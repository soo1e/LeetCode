class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(start, curr):
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for num in range(start, n+1):
                if num not in curr:
                    curr.append(num)
                    backtrack(num+1, curr)
                    curr.pop()
        
        backtrack(1, [])
        return ans