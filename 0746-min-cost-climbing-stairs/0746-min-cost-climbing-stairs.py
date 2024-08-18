from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)  # 계단의 개수를 계산
        
        # 특수 경우 처리: 계단이 1개 또는 2개인 경우
        if n == 1:
            return cost[0]  # 계단이 1개인 경우 그 계단의 비용 반환
        elif n == 2:
            return min(cost[0], cost[1])  # 계단이 2개인 경우 더 적은 비용 반환
        
        # 각 계단까지 도달하는 최소 비용을 저장할 리스트 초기화
        minCost = [0] * n
        minCost[0] = cost[0]  # 첫 번째 계단까지의 최소 비용은 cost[0]
        minCost[1] = cost[1]  # 두 번째 계단까지의 최소 비용은 cost[1]
        
        # 2번째 계단부터 n-1번째 계단까지 최소 비용을 계산
        for i in range(2, n):
            # i번째 계단까지의 최소 비용은 i-1번째 계단에서 올라오는 경우와
            # i-2번째 계단에서 올라오는 경우 중 더 작은 값을 선택
            minCost[i] = min(minCost[i-1] + cost[i], minCost[i-2] + cost[i])
        
        # 마지막 계단 또는 마지막에서 두 번째 계단에 도달하는 최소 비용 반환
        return min(minCost[-1], minCost[-2])

