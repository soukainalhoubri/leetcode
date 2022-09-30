class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        visited=set()
        def dfs(i,adjacents):
            for adj in adjacents[i]:
                if adj not in visited:
                    visited.add(adj)
                    dfs(adj,adjacents)
                    
        
        number=0
        adjacents={i:[] for i in range(n)}
        for edge in connections:
            adjacents[edge[0]].append(edge[1])
            adjacents[edge[1]].append(edge[0])
        for i in range(n):
            if i not in visited:
                number+=1
                dfs(i,adjacents)
        return number-1