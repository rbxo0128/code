import collections
import itertools
import bisect

def solution(info, query):
    info_dict = collections.defaultdict(list)

    for i_str in info:
        parts = i_str.split()
        language = parts[0]
        job = parts[1]
        career = parts[2]
        food = parts[3]
        score = int(parts[4])
        conditions = [language, job, career, food]

        for k in range(5):
            for indices_to_replace in itertools.combinations(range(4), k):
                key_parts = list(conditions)
                for idx in indices_to_replace:
                    key_parts[idx] = '-'
                key = tuple(key_parts)
                info_dict[key].append(score)

    for key in info_dict:
        info_dict[key].sort()

    answer = []
    for q_str in query:
        q_parts_raw = q_str.split(" and ")
        last_part = q_parts_raw[3].split()
        q_language = q_parts_raw[0]
        q_job = q_parts_raw[1]
        q_career = q_parts_raw[2]
        q_food = last_part[0]
        q_score = int(last_part[1])

        query_key = (q_language, q_job, q_career, q_food)

        count = 0
        if query_key in info_dict:
            scores = info_dict[query_key]
            idx = bisect.bisect_left(scores, q_score)
            count = len(scores) - idx

        answer.append(count)

    return answer
