class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in memo:
                return [memo[needed], i]
            memo[num] = i