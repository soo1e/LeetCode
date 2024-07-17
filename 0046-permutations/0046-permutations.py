# input으로 주어진 nums에 대해서 될 수 있는 모든 순열을 표현하시오

# 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtracking(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtracking(curr)
                    curr.pop()
                    
        backtracking([])
        return ans
        