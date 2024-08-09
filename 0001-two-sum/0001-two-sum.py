# 해시 테이블로 풀어보기
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 숫자와 숫자의 인덱스를 키, 밸류로 하는 빈 해시테이블을 만든다.
        list = {}

        # 반복문
        for i, num in enumerate(nums):
            # 목표 값을 만들기 위해 필요한 숫자 계산
            needed = target - num

            # 필요 숫자가 해시테이블에 존재하면 그 수의 인덱스와 현재 인덱스 반환
            if needed in list:
                return [list[needed], i]

            # 아니라면 해시테이블에 숫자와 인덱스 추가
            list[num] = i