class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            print('i :',i)
            start=0
            end=cols
            mid=start+(end-start)//2
            while start<=end:
                
                mid=start+(end-start)//2
                if not(0<=mid<cols):
                    break
                print(mid)
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]>target:
                    end=mid-1
                else:
                    start=mid+1
                
        return False

    
# #testing code:
# matrix=[[1,3]], rows=1, cols=2

# start=0,end=1

# while:
#     mid=0+1-0//2=0
#     matrix[0][0]=1!=3
    
    

