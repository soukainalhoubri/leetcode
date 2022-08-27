class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        maxdiv=1
        for i in range(2,a+1):
            if a%i==0 and b%i==0:
                maxdiv=i
        return maxdiv