from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 초기값 설정: 첫 번째 요소를 최대 합으로 초기화
        max_sum = nums[0]
        current_sum = nums[0]
        
        # 배열의 두 번째 요소부터 순회하며 최대 부분 배열 합 계산
        for i in range(1, len(nums)):
            # 현재까지의 최대 합을 계산 (이전 부분 배열 합에 현재 요소를 더한 것과 현재 요소 중 더 큰 값)
            current_sum = max(nums[i], current_sum + nums[i])
            
            # 전체 최대 합 업데이트
            max_sum = max(max_sum, current_sum)
        
        return max_sum