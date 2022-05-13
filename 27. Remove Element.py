# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

#accepted: brute forcing
#O(n^2)
def removeElement(nums, val):
        n=len(nums)
        i=0
        while(i<n):
            if nums[i]==val:
                n-=1
                del nums[i]
                i-=1
            i+=1

        return len(nums)