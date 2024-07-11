from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # visited 초기화
        visited = [False] * len(rooms)
        
        def bfs(rooms, start_v):
            visited[start_v] = True
            queue = deque()
            queue.append(start_v)
            
            while queue:
                cur_v = queue.popleft()
                for next_v in rooms[cur_v]:
                    if not visited[next_v]:
                        queue.append(next_v)
                        visited[next_v] = True
            
            # False가 존재한다면 False
            if False in visited:
                return False
            
            else:
                return True
            
        bfs(rooms, 0)
        return all(visited)