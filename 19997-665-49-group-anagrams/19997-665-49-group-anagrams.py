from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # 기본값이 리스트인 딕셔너리

        for s in strs:
            # 문자열을 정렬하여 키로 사용
            key = ''.join(sorted(s))
            anagrams[key].append(s)  # 해당 키에 원본 문자열 추가

        return list(anagrams.values())  # 그룹화된 애너그램 리스트 반환