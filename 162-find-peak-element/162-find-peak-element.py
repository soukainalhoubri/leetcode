def check_peak(nums,index):
    if len(nums)==1:
        print("condition 1")
        return True
    if (index==len(nums)-1 and nums[index]>nums[index-1]) or (index==0 and nums[index]>nums[index+1]):
        print("condition 2")
        return True
    if nums[index]>nums[index-1] and nums[index]>nums[index+1]:
        print("condition 3")
        return True
    print("condition 4")
    return False
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #strictly greater than its neighbors
        #return index
        #there can be multiple peaks, return any of them
        #nums[-1] = nums[n] = -∞
        
       # -inf [1,2,8,9,0,4,3,1,9] -inf
       #  n=9
       #  start=0
       #  end=8
       #  mid=
        n=len(nums)
        start=0
        end=n-1
        while start<=end:
            mid=(start+end)//2
            print(mid)
            if check_peak(nums,mid):
                return mid
            if nums[mid]<nums[mid+1]:
                start=mid+1
            else:
                end=mid-1