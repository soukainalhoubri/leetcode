class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #array is sorted
        #return the squares of numbers: sorted
        #items can be negative
        
#         I can use extra space
        
#         [-4,-1,0,3,10]
#         [0,1,9,16,100]
        
            # * I want to keep track of the index I want to modify
            # * The number I will be adding next
        n=len(nums)
        squares=[-1]*n
        largest_square=n-1
        left,right=0,n-1
        while left<=right:
            right_square=nums[right]**2
            left_square=nums[left]**2
            if right_square>=left_square:
                squares[largest_square]=right_square
                right-=1
            else:
                squares[largest_square]=left_square
                left+=1
            largest_square-=1
        return squares
                
                
            