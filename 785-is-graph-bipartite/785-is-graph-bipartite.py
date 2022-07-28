from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #I need to keep track of all of the node colors
        #I do BFS, and change color
        #there is no mention that the graph can't be disconnected, se we assume it can
        colors={i:-1 for i in range(len(graph))}
        n=len(graph)
        visited=set()
        colors[0]=1
        for i in range(len(graph)):
            q=deque()
            q.append(i)
            while q:
                current=q.popleft()
                visited.add(i)
                for adj in graph[current]:
                    if colors[adj]==-1:
                        colors[adj]=1-colors[current]
                    elif colors[adj]==colors[current]:
                        return False
            if len(visited)==n:
                return True
        
            