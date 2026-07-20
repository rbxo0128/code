from collections import Counter

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        str_counts = Counter(s)
        answer = []
        answer_set = set()
        for x in s:
            if x in answer_set:
                str_counts[x] -= 1
                continue

            while answer and answer[-1] > x and str_counts[answer[-1]] > 0:
                answer_set.remove(answer[-1])
                answer.pop()
                
            answer.append(x)
            answer_set.add(x)
            str_counts[x] -= 1

        return "".join(answer)