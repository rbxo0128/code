class Solution:
    def checkOverlap(self, r: int, x: int, y: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        cx = max(x1, min(x, x2))
        cy = max(y1, min(y, y2))

        if (x-cx)**2 + (y-cy)**2 <= r ** 2:
            return True

        return False