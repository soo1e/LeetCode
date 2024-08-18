from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP 테이블 초기화: 크기는 (amount + 1), 초기값은 무한대
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 금액 0을 만들기 위한 동전 수는 0
        
        # 각 금액에 대해 최소 동전 수 계산
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # dp[amount]가 여전히 무한대라면, 해당 금액을 만들 수 없다는 의미
        return dp[amount] if dp[amount] != float('inf') else -1
