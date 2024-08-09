# 해시 테이블로 풀어보기

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in list:
                return [list[needed], i]
            
            list[num] = i