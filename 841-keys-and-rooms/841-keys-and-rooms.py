from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q=deque()
        n=len(rooms)
        q.append(0)
        visited=set()
        visitable=set(rooms[0])
        visitable.add(0)
        while q:
            current=q.popleft()
            visited.add(current)
            for i in rooms[current]:
                if i not in visited:
                    q.append(i)
            if current in visitable:
                for i in rooms[current]:
                    visitable.add(i)
        
        return len(visitable)==n