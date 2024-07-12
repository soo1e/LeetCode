from collections import deque
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        # BFS를 위한 큐 초기화
        queue = deque([(0, 0)])  # (현재 금액, 동전 수)
        visited = set()  # 방문한 금액을 추적하기 위한 집합

        while queue:
            current_amount, num_coins = queue.popleft()
            
            for coin in coins:
                next_amount = current_amount + coin
                
                if next_amount == amount:
                    return num_coins + 1
                
                if next_amount < amount and next_amount not in visited:
                    visited.add(next_amount)
                    queue.append((next_amount, num_coins + 1))
        
        return -1  # 모든 경우를 탐색했으나 금액을 만들 수 없는 경우