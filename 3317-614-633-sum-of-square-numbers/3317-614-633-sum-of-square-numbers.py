import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(0, int(math.isqrt(c)) + 1):  # a^2 <= c
            b_squared = c - a * a
            b = int(math.isqrt(b_squared))
            if b * b == b_squared:
                return True
        return False
