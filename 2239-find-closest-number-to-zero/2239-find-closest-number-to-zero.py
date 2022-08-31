class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans=min([abs(i) for i in nums])
        if ans in nums:
            return ans
        return -ans