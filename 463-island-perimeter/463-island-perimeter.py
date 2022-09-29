class Solution:
    answer=0
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def get_land(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1:
                        return [i,j]
        sr,sc=get_land(grid)
        n=len(grid)
        m=len(grid[0])
        visited=set()
        def dfs(sr,sc):
            print("got in")
            neighbors=[[sr-1,sc],[sr+1,sc],[sr,sc-1],[sr,sc+1]]
            visited.add((sr,sc))
            for adj in neighbors:
                print("adj",adj)
                if not (0<=adj[0]<n and 0<=adj[1]<m) or grid[adj[0]][adj[1]]==0:
                    print('got here')
                    self.answer+=1
                elif grid[adj[0]][adj[1]]==1:
                    if (adj[0],adj[1]) not in visited:
                        dfs(adj[0],adj[1])
            return
        dfs(sr,sc)
        return self.answer
        
        
        
        #there is exactly one issland
        #the water does not have lakes
        
#         [[1]] => 4
#         [[1,1]] => 6
#         [[1,0]] => 4
        
#         [[0,1,0,0],
#          [1,1,1,0], ==> 16
#          [0,1,0,0],
#          [1,1,0,0]] 
        
        #Do i need to start my dfs from a land or n.i.?
        #mY CURRENT VALUE IS 1
        
        #find a 1, use it as a start, beause I don't want to dfs over the whole
        
        
        
        
        