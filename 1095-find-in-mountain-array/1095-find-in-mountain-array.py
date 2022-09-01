# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

def peak(arr,start,end):
    while start<=end:
        mid=(start+end)//2
        if arr.get(mid)>arr.get(mid-1) and arr.get(mid)>arr.get(mid+1):
            return mid
        elif arr.get(mid)>arr.get(mid+1):
            end=mid-1
            
        else:
            start=mid+1
def binarySearch(arr,start,end,target,left):
    print("executing search for ",start,end)
    if (target<arr.get(start) and left) or (target>arr.get(end-1) and not left):
        return -1
    while start<=end:
        mid=(start+end)//2
        print("mid ",mid)
        if arr.get(mid)==target:
            
            return mid
        if left:
            if arr.get(mid)<target:
                start=mid+1
            else:
                end=mid-1
        else:
            if arr.get(mid)<target:
                end=mid-1
            else:
                start=mid+1
        
    return -1
class Solution:
    def findInMountainArray(self, target: int, A: 'MountainArray') -> int:
        n = A.length()
        # find index of peak
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if A.get(m) < A.get(m + 1):
                l = peak = m + 1
            else:
                r = m
        # find target in the left of peak
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            if A.get(m) < target:
                l = m + 1
            elif A.get(m) > target:
                r = m - 1
            else:
                return m
        # find target in the right of peak
        l, r = peak, n - 1
        while l <= r:
            m = (l + r) // 2
            if A.get(m) > target:
                l = m + 1
            elif A.get(m) < target:
                r = m - 1
            else:
                return m
        return -1
        
            