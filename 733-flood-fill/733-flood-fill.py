class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R=len(image)
        C=len(image[0])
        original=image[sr][sc]
        def dfs(r,c):
            if(not(0<=r<R and 0<=c<C))or image[r][c]!=original:
                return
            image[r][c]=color
            [dfs(r+x,c+y) for (x,y) in [(1,0),(-1,0),(0,1),(0,-1)]]
        if original!=color:
            dfs(sr,sc)
        return image
    
    