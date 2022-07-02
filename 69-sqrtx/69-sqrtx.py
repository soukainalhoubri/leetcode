class Solution:
    def mySqrt(self, x: int) -> int:
        start=0
        end=x
        while start<=x:
            mid=start+(end-start)//2
            if mid*mid<=x<(mid+1)*(mid+1):
                return mid
            elif mid*mid<x:
                start=mid+1
            else:
                end=mid-1