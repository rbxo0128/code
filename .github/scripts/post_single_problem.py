#!/usr/bin/env python3
"""
단일 문제 포스팅 스크립트
환경변수: BLOG_API_URL, BLOG_API_KEY, PROBLEM_PATH
"""

import os
import re
import json
import requests
from pathlib import Path
from typing import Dict, Optional


def parse_readme(readme_path: Path) -> Dict:
    """README.md 파싱"""
    content = readme_path.read_text(encoding='utf-8')
    
    data = {
        'platform': 'BOJ',
        'problemId': '',
        'problemTitle': '',
        'tierName': '',
        'tags': [],
        'problemUrl': ''
        'content' : content
    }
    
    # 제목: # [Gold IV] 고층 건물 - 1027
    title_match = re.search(r'#\s*\[([^\]]+)\]\s*(.+?)\s*-\s*(\d+)', content)
    if title_match:
        data['tierName'] = title_match.group(1).strip()
        data['problemTitle'] = title_match.group(2).strip()
        data['problemId'] = title_match.group(3).strip()
    
    # 문제 링크
    link_match = re.search(r'\[문제 링크\]\((https://[^\)]+)\)', content)
    if link_match:
        data['problemUrl'] = link_match.group(1)
    
    # 분류 (태그)
    tags_section = re.search(r'### 분류\s*\n\s*(.+)', content)
    if tags_section:
        tags_text = tags_section.group(1).strip()
        data['tags'] = [tag.strip() for tag in tags_text.split(',')]
    
    return data


def find_solution_file(problem_dir: Path) -> Optional[Path]:
    """풀이 코드 파일 찾기"""
    extensions = ['.py', '.java', '.cpp', '.c', '.js', '.kt', '.swift', '.go', '.rs']
    
    for ext in extensions:
        files = list(problem_dir.glob(f'*{ext}'))
        if files:
            return files[0]
    
    return None


def detect_language(file_path: Path) -> str:
    """파일 확장자로 언어 감지"""
    ext = file_path.suffix.lower()
    language_map = {
        '.py': 'Python 3',
        '.java': 'Java',
        '.cpp': 'C++',
        '.c': 'C',
        '.js': 'JavaScript',
        '.kt': 'Kotlin',
        '.swift': 'Swift',
        '.go': 'Go',
        '.rs': 'Rust'
    }
    return language_map.get(ext, 'Unknown')


def post_to_blog(problem_data: Dict, code: str, language: str) -> bool:
    """블로그에 포스팅"""
    
    blog_api_url = os.environ.get('BLOG_API_URL')
    blog_api_key = os.environ.get('BLOG_API_KEY')
    
    if not blog_api_url or not blog_api_key:
        print("❌ Missing environment variables: BLOG_API_URL or BLOG_API_KEY")
        return False
    
    payload = {
        'code': code,
        'language': language,
        **problem_data
    }
    
    headers = {
        'Content-Type': 'application/json',
        'X-API-Key': blog_api_key
    }
    
    print(f"\n📤 포스팅 중...")
    print(f"   제목: [{problem_data['tierName']}] {problem_data['problemTitle']} - {problem_data['problemId']}")
    print(f"   태그: {', '.join(problem_data['tags'])}")
    print(f"   언어: {language}")
    
    try:
        response = requests.post(
            blog_api_url,
            json=payload,
            headers=headers,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"\n✅ 포스팅 성공!")
            print(f"   Post ID: {result.get('postId')}")
            print(f"   제목: {result.get('title')}")
            return True
        else:
            print(f"\n❌ 포스팅 실패: HTTP {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"\n❌ 포스팅 중 오류 발생: {e}")
        return False


def main():
    """메인 함수"""
    
    problem_path = os.environ.get('PROBLEM_PATH')

    if not problem_path:
        print("❌ PROBLEM_PATH environment variable not set")
        return

    problem_dir = Path(problem_path)
    
    if not problem_dir.exists():
        print(f"❌ Problem directory not found: {problem_dir}")
        return
    
    # README.md 파싱
    readme_path = problem_dir / 'README.md'
    if not readme_path.exists():
        print(f"❌ README.md not found: {readme_path}")
        return
    
    print(f"\n📂 문제 경로: {problem_dir}")
    
    problem_data = parse_readme(readme_path)
    
    # 풀이 코드 찾기
    solution_file = find_solution_file(problem_dir)
    if not solution_file:
        print(f"❌ Solution file not found in {problem_dir}")
        return
    
    print(f"📄 풀이 파일: {solution_file.name}")
    
    code = solution_file.read_text(encoding='utf-8')
    language = detect_language(solution_file)
    
    print(f"💻 언어: {language}")
    print(f"📏 코드 길이: {len(code)}자, {len(code.split(chr(10)))}줄")
    
    # 블로그에 포스팅
    success = post_to_blog(problem_data, code, language)
    
    if success:
        print("\n" + "="*60)
        print("✨ 모든 작업이 완료되었습니다!")
        print("="*60)
    else:
        print("\n" + "="*60)
        print("❌ 포스팅에 실패했습니다.")
        print("="*60)
        exit(1)


if __name__ == '__main__':
    main()