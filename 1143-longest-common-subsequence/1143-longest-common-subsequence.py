from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # text1의 길이 m, text2의 길이 n
        m, n = len(text1), len(text2)
        
        # DP 테이블 초기화: (m+1) x (n+1) 크기, 초기값은 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # DP 테이블 채우기
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # 문자가 같으면, dp[i][j] = dp[i-1][j-1] + 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 문자가 다르면, dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # 최종 결과는 dp[m][n]에 저장됨
        return dp[m][n]
