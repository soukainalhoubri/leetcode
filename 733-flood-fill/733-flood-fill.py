class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #current_color need to be saved
        #some sort of recursion here
        initial_color=image[sr][sc]
        n=len(image)
        m=len(image[0])
        if color==initial_color:
            return image
        def recursion(image, sr, sc):
            #deal with the neighbors of the current cell
            image[sr][sc]=color
            neighbors=[[sr-1,sc],[sr+1,sc],[sr,sc-1],[sr,sc+1]]
            for adj in neighbors:
                if 0<=adj[0]<n and 0<=adj[1]<m and image[adj[0]][adj[1]]==initial_color:
                    recursion(image, adj[0], adj[1])
            return
        recursion(image,sr,sc)
        
        return image
        