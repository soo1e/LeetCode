from bisect import bisect_left

class Solution:
    def search(self, nums, target):
        idx = bisect_left(nums, target)
        if idx != len(nums) and nums[idx] == target:
            return idx
        
        return -1
