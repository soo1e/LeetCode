class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP 테이블 초기화: 모든 값이 0인 m x n 크기의 2D 배열
        dp = [[0] * n for _ in range(m)]
        
        # 첫 번째 행과 첫 번째 열은 모두 1로 초기화
        for i in range(m):
            dp[i][0] = 1  # 첫 번째 열의 경로 수는 1
        for j in range(n):
            dp[0][j] = 1  # 첫 번째 행의 경로 수는 1
        
        # DP 테이블 채우기
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  # 위에서 오는 경로 + 왼쪽에서 오는 경로
        
        # 마지막 위치의 경로 수 반환
        return dp[m-1][n-1]