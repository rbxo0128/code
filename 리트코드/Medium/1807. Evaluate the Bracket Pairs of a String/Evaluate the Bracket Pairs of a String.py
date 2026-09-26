class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        l = len(s)
        words = []
        idx_map = {}
        idx = 0
        start = False
        word = []
        for i in range(l):
            if s[i] == "(":
                if word:
                    w = "".join(word)
                    words.append(w)
                    idx += 1

                word = []
                start = True

            elif start and s[i] == ")":
                if word:
                    w = "".join(word)
                    if w in idx_map:
                        idx_map[w].append(idx)
                    else:
                        idx_map[w] = [idx]
                    idx += 1
                    words.append("")
                
                word = []
                start = False

            else:
                word.append(s[i])
        if word:
            w = "".join(word)
            words.append(w)
        
        for x,y in knowledge:
            if x in idx_map:
                for i in idx_map[x]:
                    words[i] = y

        for i in range(len(words)):
            if not words[i]:
                words[i] = "?"

        return "".join(words)