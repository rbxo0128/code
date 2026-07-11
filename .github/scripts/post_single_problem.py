#!/usr/bin/env python3
"""Post one algorithm problem directory to the blog API.

Required environment variables:
- PROBLEM_PATH
- BLOG_API_URL and BLOG_API_KEY, unless DRY_RUN=true

Optional:
- BLOG_PROXY
- DRY_RUN=true|false
"""

from __future__ import annotations

import html
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, Optional

import requests

PLATFORM_LABELS = {
    "백준": "백준",
    "프로그래머스": "프로그래머스",
    "리트코드": "리트코드",
}

LANGUAGE_MAP = {
    ".py": "Python 3",
    ".java": "Java",
    ".cpp": "C++",
    ".c": "C",
    ".cs": "C#",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".kt": "Kotlin",
    ".swift": "Swift",
    ".go": "Go",
    ".rs": "Rust",
    ".sql": "SQL",
    ".php": "PHP",
    ".rb": "Ruby",
    ".scala": "Scala",
    ".dart": "Dart",
    ".sh": "Bash",
    ".rkt": "Racket",
    ".ex": "Elixir",
    ".erl": "Erlang",
    ".cj": "Cangjie",
}

LEETCODE_DIFFICULTY_LABELS = {
    "Easy": "쉬움",
    "Medium": "보통",
    "Hard": "어려움",
}


def normalize_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def strip_html(value: str) -> str:
    return normalize_whitespace(html.unescape(re.sub(r"<[^>]+>", "", value)))


def unique(values: Iterable[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        cleaned = normalize_whitespace(value)
        if cleaned and cleaned not in seen:
            seen.add(cleaned)
            result.append(cleaned)
    return result


def detect_platform(problem_dir: Path) -> str:
    for part in problem_dir.parts:
        if part in PLATFORM_LABELS:
            return PLATFORM_LABELS[part]
    raise ValueError(f"지원하지 않는 문제 경로입니다: {problem_dir}")


def parse_folder_name(problem_dir: Path) -> tuple[str, str]:
    match = re.match(r"^\s*(\d+)\.\s*(.+?)\s*$", problem_dir.name)
    if not match:
        return "", normalize_whitespace(problem_dir.name)
    return match.group(1), normalize_whitespace(match.group(2))


def parse_markdown_section(content: str, heading: str) -> str:
    match = re.search(
        rf"^###\s*{re.escape(heading)}\s*$\s*(.*?)(?=^###\s|\Z)",
        content,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def split_tags(value: str) -> list[str]:
    plain = strip_html(value)
    return unique(re.split(r"\s*,\s*|\s*>\s*", plain))


def parse_tags_from_root_readme(problem_dir: Path, problem_id: str) -> list[str]:
    try:
        repo_root = problem_dir.parents[2]
    except IndexError:
        return []

    root_readme = repo_root / "README.md"
    if not root_readme.exists() or not problem_id:
        return []

    content = root_readme.read_text(encoding="utf-8")

    # Single-table format.
    row_match = re.search(
        rf"^\|\s*{re.escape(problem_id)}\s*\|.*?\|\s*([^|]+?)\s*\|\s*$",
        content,
        flags=re.MULTILINE,
    )
    if row_match:
        return split_tags(row_match.group(1))

    # Legacy topic sections.
    tags: list[str] = []
    current_topic = ""
    for line in content.splitlines():
        if line.startswith("## "):
            current_topic = line[3:].strip()
        elif current_topic and re.search(rf"\[{re.escape(problem_id)}\.\s", line):
            tags.append(current_topic)
    return unique(tags)


def parse_readme(readme_path: Path, problem_dir: Path) -> Dict[str, Any]:
    content = readme_path.read_text(encoding="utf-8")
    platform = detect_platform(problem_dir)
    folder_id, folder_title = parse_folder_name(problem_dir)

    data: Dict[str, Any] = {
        "platform": platform,
        "problemId": folder_id,
        "problemTitle": folder_title,
        "tierName": problem_dir.parent.name,
        "tags": [],
        "content": content,
    }

    # BaekjoonHub / Programmers heading: # [Gold IV] title - 1027
    heading_match = re.search(
        r"^#\s*\[([^\]]+)\]\s*(.+?)\s*-\s*(\d+)\s*$",
        content,
        flags=re.MULTILINE,
    )
    if heading_match:
        data["tierName"] = normalize_whitespace(heading_match.group(1))
        data["problemTitle"] = normalize_whitespace(heading_match.group(2))
        data["problemId"] = heading_match.group(3)

    # LeetCode heading: <h2><a ...>2095. Title</a></h2><h3>Medium</h3>
    if platform == "리트코드":
        title_match = re.search(
            r"<h2>\s*<a\b[^>]*>\s*(\d+)\.\s*(.*?)\s*</a>\s*</h2>",
            content,
            flags=re.IGNORECASE | re.DOTALL,
        )
        if title_match:
            data["problemId"] = title_match.group(1)
            data["problemTitle"] = strip_html(title_match.group(2))

        difficulty_match = re.search(
            r"<h3>\s*([^<]+?)\s*</h3>",
            content,
            flags=re.IGNORECASE,
        )
        if difficulty_match:
            difficulty = normalize_whitespace(difficulty_match.group(1))
            data["tierName"] = difficulty

    classification = parse_markdown_section(content, "분류")
    if classification:
        data["tags"] = split_tags(classification)

    # Programmers uses '구분' rather than '분류'. Keep the most specific category.
    if not data["tags"] and platform == "프로그래머스":
        category = parse_markdown_section(content, "구분")
        categories = split_tags(category)
        if categories:
            data["tags"] = [categories[-1]]

    # Existing LeetCode README files may not have a classification section yet.
    if not data["tags"] and platform == "리트코드":
        data["tags"] = parse_tags_from_root_readme(problem_dir, data["problemId"])

    if not data["problemId"] or not data["problemTitle"]:
        raise ValueError(f"문제 번호 또는 제목을 파싱하지 못했습니다: {readme_path}")

    return data


def find_solution_file(problem_dir: Path) -> Optional[Path]:
    candidates = [
        path
        for path in problem_dir.iterdir()
        if path.is_file() and path.suffix.lower() in LANGUAGE_MAP
    ]
    return sorted(candidates, key=lambda path: path.name.lower())[0] if candidates else None


def detect_language(file_path: Path) -> str:
    return LANGUAGE_MAP.get(file_path.suffix.lower(), "Unknown")


def print_summary(problem_data: Dict[str, Any], solution_file: Path, language: str) -> None:
    tier = problem_data["tierName"]
    display_tier = (
        LEETCODE_DIFFICULTY_LABELS.get(tier, tier)
        if problem_data["platform"] == "리트코드"
        else tier
    )
    print(f"📂 플랫폼: {problem_data['platform']}")
    print(f"📌 문제: [{display_tier}] {problem_data['problemTitle']} - {problem_data['problemId']}")
    print(f"🏷 분류: {', '.join(problem_data['tags']) or '-'}")
    print(f"📄 풀이 파일: {solution_file.name}")
    print(f"💻 언어: {language}")


def post_to_blog(problem_data: Dict[str, Any], code: str, language: str) -> bool:
    dry_run = os.environ.get("DRY_RUN", "false").lower() == "true"
    payload = {"code": code, "language": language, **problem_data}

    if dry_run:
        print("\n📋 미리보기 모드 — API를 호출하지 않습니다.")
        print(json.dumps(payload, ensure_ascii=False, indent=2)[:5000])
        return True

    blog_api_url = os.environ.get("BLOG_API_URL")
    blog_api_key = os.environ.get("BLOG_API_KEY")
    blog_proxy = os.environ.get("BLOG_PROXY")

    if not blog_api_url or not blog_api_key:
        print("❌ BLOG_API_URL 또는 BLOG_API_KEY가 없습니다.")
        return False

    headers = {
        "Content-Type": "application/json",
        "X-API-Key": blog_api_key,
    }
    if blog_proxy:
        headers["X-Proxy-Secret"] = blog_proxy

    try:
        response = requests.post(
            blog_api_url,
            json=payload,
            headers=headers,
            timeout=180,
        )
    except requests.RequestException as exc:
        print(f"❌ 포스팅 요청 중 오류 발생: {exc}")
        return False

    if 200 <= response.status_code < 300:
        try:
            result = response.json()
        except ValueError:
            result = {}
        print("✅ 포스팅 성공")
        if result.get("postId") is not None:
            print(f"   Post ID: {result['postId']}")
        if result.get("title"):
            print(f"   제목: {result['title']}")
        return True

    print(f"❌ 포스팅 실패: HTTP {response.status_code}")
    print(f"   Response: {response.text[:2000]}")
    return False


def main() -> int:
    problem_path = os.environ.get("PROBLEM_PATH")
    if not problem_path:
        print("❌ PROBLEM_PATH 환경변수가 없습니다.")
        return 1

    problem_dir = Path(problem_path)
    if not problem_dir.is_dir():
        print(f"❌ 문제 폴더가 없습니다: {problem_dir}")
        return 1

    readme_path = problem_dir / "README.md"
    if not readme_path.exists():
        print(f"❌ README.md가 없습니다: {readme_path}")
        return 1

    solution_file = find_solution_file(problem_dir)
    if solution_file is None:
        print(f"❌ 풀이 코드 파일이 없습니다: {problem_dir}")
        return 1

    try:
        problem_data = parse_readme(readme_path, problem_dir)
        code = solution_file.read_text(encoding="utf-8")
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"❌ 문제 파일 처리 실패: {exc}")
        return 1

    language = detect_language(solution_file)
    print_summary(problem_data, solution_file, language)
    print(f"📏 코드 길이: {len(code)}자, {len(code.splitlines())}줄")

    return 0 if post_to_blog(problem_data, code, language) else 1


if __name__ == "__main__":
    sys.exit(main())
