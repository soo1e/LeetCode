class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        longest_streak = 0

        for num in nums_set:
            # 시작점 찾기: num-1이 존재하지 않으면 num은 수열의 시작점
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                # 연속된 수가 존재하는지 확인하여 수열 길이 계산
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                # 최대 길이 갱신
                longest_streak = max(longest_streak, current_streak)

        return longest_streak