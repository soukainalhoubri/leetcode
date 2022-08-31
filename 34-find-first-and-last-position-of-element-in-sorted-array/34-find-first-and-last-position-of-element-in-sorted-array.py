def binarySearch(nums,target,findmax):
    start,end=0,len(nums)-1
    index=-1
    while start<=end:
        mid=(start+end)//2
        if target<nums[mid]:
            end=mid-1
        elif target>nums[mid]:
            start=mid+1
        else:
            index=mid
            if findmax:
                start=mid+1
            else:
                end=mid-1
    return index
    
    
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result=[-1,-1]
        result[0]=binarySearch(nums,target,False)
        # result[1]=result[0]
        if result[0]!=-1:
            result[1]=binarySearch(nums,target,True)
        return result