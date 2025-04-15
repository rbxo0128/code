def solution(gems):
    gem = set(gems)
    l = len(gem)
    count = {}
    left = 0
    d = len(gems)
    answer = [0, d - 1]

    for right in range(d):
        count[gems[right]] = count.get(gems[right], 0) + 1

        while len(count) == l:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]

            count[gems[left]] -= 1
            if count[gems[left]] == 0:
                del count[gems[left]]
            left += 1

    return [answer[0] + 1, answer[1] + 1]
