import sys
from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):

        # 방향 그래프로 변경
        course_visited = []
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # 이 문제에서 prerequisites의 원소 [v, u]는 u->v 의 방향을 가진 edge를 뜻한다.
        for v, u in prerequisites:
            graph[u].append(v)
            # indegree 기록
            indegree[v] += 1

        # 위상정렬 수행
        # indegree == 0인 정점부터 탐색 시작
        q = deque()
        for v in range(numCourses):
            if indegree[v] == 0:
                q.append(v)
        while q:
            cur_v = q.popleft()
            # cur_v에 해당하는 과목을 수강한 것.
            course_visited.append(cur_v)

            # 해당 정점과 연결된 노드들의 진입차수에서 1빼기
            for next_v in graph[cur_v]:
                indegree[next_v] -= 1

                # 진입차수가 0이면 이제 수강해도 된다는 뜻이기 때문에 queue에 ㅊㅜ가
                if indegree[next_v] == 0:
                    q.append(next_v)

                # 위상정렬 수행 후 들은 과목수와 numCourse가 같은지 반환
                # 사이클이 존재한다면 모든 과목을 방문하지 못하는 것이기 때문에 numCourse와 다르다.
        return len(course_visited) == numCourses