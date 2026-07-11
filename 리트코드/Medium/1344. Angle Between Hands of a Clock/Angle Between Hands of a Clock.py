class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = 30 * (hour%12) + 0.5 * minutes
        minute_angle = 6 * minutes
        answer = abs(minute_angle-hour_angle)
        return answer if answer < 180 else 360-answer