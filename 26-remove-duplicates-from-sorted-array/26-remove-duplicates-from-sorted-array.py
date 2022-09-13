class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #sorted
        #remove duplicates in place
        #output must be ordered as well
        
        #I need to iterate over the array and I need to keep track of the repeatd number
#          i   j
#         [0,0,1,1,1,2,2,3,3,4]
        
#         #I want to keep track of two things: the index I want to change, and the first number which is not repeated while movng
#         j=1
#                i           j     
#         [0,1,2,3,4,2,2,3,3,4]I should keep finding the first number which is stricty larer that i
        n=len(nums)
        i,j=0,1
        while i<n-1 and j<n:
            if nums[i]<nums[j]:
                nums[i+1]=nums[j]
                i+=1
            j+=1
        return i+1