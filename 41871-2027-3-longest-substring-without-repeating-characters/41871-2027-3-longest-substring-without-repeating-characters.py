class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        answer = 0
        n = len(s)
        #✅ 시작점을 0으로 초기화한다.
        start = 0
        #✅ 문자가 범위에 포함되었는지를 확인할 해시셋을 선언한다.
        counter = set()
        #✅ 문자열의 맨 앞 문자부터 끝점으로 삼으며 순회한다.
        for i, char in enumerate(s):
            if char in counter:
                answer = max(answer, i-start)
		            #✅ 끝점의 문자가 해시셋에서 빠져나올때까지 반복한다.
                while char in counter:
				            #✅ 시작점 문자를 해시셋에서 제거하고 시작점을 한칸 옮긴다.
                    counter.remove(s[start])
                    start += 1
		        #✅ 끝점 문자를 해시셋에 추가한다.
            counter.add(char)
		    #✅ 최대 길이를 업데이트한다.
        answer = max(answer, n-start)
        return answer