from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()

        # 가능한 모든 3자리 순열 생성
        for perm in permutations(digits, 3):
            # 앞자리가 0이면 스킵
            if perm[0] == 0:
                continue

            # 마지막 숫자가 짝수인지 확인
            if perm[2] % 2 != 0:
                continue

            # 세 자리 수로 변환
            num = perm[0] * 100 + perm[1] * 10 + perm[2]
            result.add(num)

        return sorted(result)
