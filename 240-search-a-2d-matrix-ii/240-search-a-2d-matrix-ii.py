class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        r,c=0,cols-1
        while 0<=r<rows and 0<=c<cols:
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                r+=1
            else:
                c-=1
        return False