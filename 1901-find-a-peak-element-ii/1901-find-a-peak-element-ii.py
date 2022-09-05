def check_peak(mat,i,j):
#     if len(mat)==1 and len(mat[0])==1:
#         print("condition 1")
#         return True
#     #check peak 
#     n=len(mat)
#     m=len(mat[0])
    
#     if mat[i][j]>mat[i][j+1] and mat[i][j]>mat[i][j-1] and mat[i][j]>mat[i-1][j] and mat[i][j]>mat[i+1][j]:
#         return True
    
        
        
    
    #return false anyways
    return False
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        #peak: greater to all its adjacent: n,s,e,w
        #no two adjacent cells are equal
        #I can find any peak-> there might be many
        #do i guarantee i have it
        #return the coordinates
#         n=len(mat)
#         m=len(mat[0])
#         for i in range(n):
#             start,end=0,m-1
#             while start<=end:
#                 mid=(start+end)//2
#                 if check_peak(mat,i,mid):
#                     return [i,j]
#                 elif mat[i][mid]<mat[i][mid+1]:
#                     start=mid+1
#                 else:
#                     end=mid-1
        top = 0
        bottom = len(mat)-1
        while bottom > top:
            mid = (top + bottom) // 2
            if max(mat[mid]) > max(mat[mid+1]):
                bottom = mid
            else:
                top = mid+1
        return [bottom,mat[bottom].index(max(mat[bottom]))]
                    