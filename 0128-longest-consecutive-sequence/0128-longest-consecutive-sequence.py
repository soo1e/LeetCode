class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        
        for num in num_set:
            if num - 1 not in num_set:
                cnt = 1
                target = num + 1
                while target in num_set:
                    target += 1
                    cnt += 1
                longest = max(longest, cnt)
        return longest