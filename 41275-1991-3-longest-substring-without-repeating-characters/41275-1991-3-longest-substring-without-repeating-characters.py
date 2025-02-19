class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # 현재 윈도우 내의 문자들을 저장할 집합
        
        left = 0  # 윈도우의 시작점
        max_length = 0  # 최대 길이

        for right in range(len(s)):  # `right`는 윈도우의 끝점을 가리킴
            while s[right] in char_set:  # 중복된 문자가 있을 때
                char_set.remove(s[left])  # 중복된 문자 제거
                left += 1  # 윈도우 시작점을 오른쪽으로 이동
            char_set.add(s[right])  # 새로운 문자를 윈도우에 추가
            max_length = max(max_length, right - left + 1)  # 최대 길이 갱신

        return max_length  # 최대 길이 반환
