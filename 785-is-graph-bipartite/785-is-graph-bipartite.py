from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #graph: undirected, unconnected, 
        #BFS, i will iterate over every node, olor it, and then go through its neghbors.
        
        visited=set()
        colors ={0:1}
        for i in range(len(graph)):
            if i not in colors:
                colors[i]=1
            q=deque()
            q.append(i)
            while q:
                current=q.popleft()
                visited.add(current)
                for adj in graph[current]:
                    if adj in colors and colors[adj]==colors[current]:
                        return False
                    colors[adj]=1-colors[current]
                    if adj not in visited:
                        q.append(adj)
            if len(visited)==len(graph):
                return True
        return True
        '''
        if they're colored with same color, I return False, else, I olor them with a different color
        '''
        '''
        
        for instance:
        
        0: A: visited
        1: B: 
        2:B
        3:B
        => False
        
        0:
        
        
        
        '''