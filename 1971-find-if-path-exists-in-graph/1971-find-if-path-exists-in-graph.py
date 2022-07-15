from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False]*n 
        neighbors={}
        for edge in edges:
            if edge[0] in neighbors:
                neighbors[edge[0]].append(edge[1])
            else:
                neighbors[edge[0]]=[edge[1]]
            
            if edge[1] in neighbors:
                neighbors[edge[1]].append(edge[0])
            else:
                neighbors[edge[1]]=[edge[0]]
        
        #start the bfs:
        q=deque()
        q.append(source)
        while q:
            current=q.popleft()
            if current == destination:  #if its the end then we can return True
                return True
            elif current in neighbors and not visited[current]:
                q.extend(neighbors[current]) 
            visited[current] = True  
        return False