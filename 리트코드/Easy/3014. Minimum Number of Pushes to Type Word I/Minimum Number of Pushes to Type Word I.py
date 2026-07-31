from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        count_list = sorted(count.items(), key = lambda x:-x[1])
        cnt = 0
        idx = 1
        answer = 0
        for x,y in count_list:
            answer += idx * y
            cnt += 1
            if cnt == 8:
                cnt = 0
                idx += 1

        return answer