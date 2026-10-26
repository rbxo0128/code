class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def days(txt):
            month = int(txt[:2])
            day = int(txt[3:])

            return sum(months[:month-1]) + day

        aa = days(arriveAlice)
        ab = days(arriveBob)
        la = days(leaveAlice)
        lb = days(leaveBob)

        start = max(aa,ab)
        end = min(la,lb)
        
        return max(0, end - start + 1)