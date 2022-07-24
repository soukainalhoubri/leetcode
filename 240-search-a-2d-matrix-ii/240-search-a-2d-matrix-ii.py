class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #bruteforce solution O(m*n)
        #we can think of dfs & bfs but that would be way more expensive in terms of time complexity O(m*n+ E)
        
        # 2D binary search:
        
        #initialize my start ad ending cordinates for both directions
        #start from center element, compare the current value to the target, and then move both directions accoringly.
        
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
        
#         rows,cols=len(matrix),len(matrix[0])
#         start_row,end_row=0,rows-1
#         start_col,end_col=0,cols-1
#         while start_row<=end_row and start_col<=end_col:
#             mid_row=start_row+(end_row-start_row)//2
#             mid_col=start_col+(end_col-start_col)//2
#             print(matrix[mid_row][mid_col])
#             if matrix[mid_row][mid_col]==target:
#                 print(matrix[mid_row][mid_col])
#                 return True
#             if target<matrix[mid_row][mid_col]:
#                 end_row=mid_row-1
                
#             else:
#                 start_row=mid_row+1
#             if matrix[mid_row][mid_col]==target:
#                 print(matrix[mid_row][mid_col])
#                 return True
                
#             if target<matrix[mid_row][mid_col]:
#                 end_col=mid_col-1
#             else:
#                 start_col=mid_col-1
#             if matrix[mid_row][mid_col]==target:
#                 print(matrix[mid_row][mid_col])
#                 return True
        
                
                
#         return False