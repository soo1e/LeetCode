import sys
import heapq


class Solution:
    def smallestRange(self, nums):
        # nums[idx]의 원소들이 몇 번째 리스트에 속해있는지 알기 쉽도록 "값 => [값, idx]" 변경
        # 원소에 배열 번호 추가
        for i in range(len(nums)):
            nums[i] = [[val, i] for val in nums[i]]

        # 초기 힙 구성 및 최대값 계산
        pq = []
        max_val = -sys.maxsize
        # 각 리스트의 첫 번째 원소들을 우선순위 큐에 입력
        for i in range(len(nums)):
            heapq.heappush(pq, nums[i][0])
            # 입력하는 과정 중 원소들의 최댓값 기록
            max_val = max(max_val, nums[i][0][0])

        # 우선순위 큐로 얻은 최솟값과 기록된 최댓값을 통해 범위 기록
        answer = [pq[0][0], max_val]
        index_list = [0] * len(nums)

        # 최소 범위 계산
        while True:
            min_val, idx = heapq.heappop(pq)
            index_list[idx] += 1

            # 각 리스트의 원소 중 한 원소가 마지막 값에 도달할 때까지 반복
            # 종료 조건
            if index_list[idx] == len(nums[idx]):
                break

            next_num = nums[idx][index_list[idx]]
            # 우선순위 큐에서 제거된 값이 존재하던 리스트에서 다음 값을 찾아 우선순위 큐에 저장
            heapq.heappush(pq, next_num)
            # 입력하는 과정 중 최댓값을 갱신
            max_val = max(max_val, next_num[0])

            # 우선순위 큐로 얻은 최솟값과 기록된 최댓값을 통해 범위 기록
            if max_val - pq[0][0] < answer[1] - answer[0]:
                answer = [pq[0][0], max_val]

        return answer