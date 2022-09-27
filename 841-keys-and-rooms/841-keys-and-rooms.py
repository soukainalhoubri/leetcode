from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #this is like checking if my graph is disconnected
        #I will start with node 0, and then visit all of its neighbors, I keep track of visited nodes and so on.
        #I will use a queue to enqueue the node to be proccessed, if it gets emptied without visiting all of the nodes, this means I can't visit all of the nodes
        visited=set()
        q=deque()
        q.append(0)
        while q:
            current=q.popleft()
            visited.add(current)
            for room in rooms[current]:
                if room not in visited:
                    q.append(room)
        return len(visited)==len(rooms)