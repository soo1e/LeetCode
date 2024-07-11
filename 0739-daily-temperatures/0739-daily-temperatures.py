from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for day, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_day = stack.pop()[0]
                ans[prev_day] = day - prev_day
            stack.append((day, temp))
        return ans