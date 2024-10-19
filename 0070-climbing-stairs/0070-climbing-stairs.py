class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Base cases
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        # 메모 딕셔너리 
        memo = {1: 1, 2: 2}

        # 반복문을 통해 memo 딕셔너리 채워주기
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[n]