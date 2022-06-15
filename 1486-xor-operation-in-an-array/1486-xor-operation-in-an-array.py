class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        nums=[start+2*i for i in range(n)]
        ans=nums[0]
        for k in nums[1:]:
            ans=ans^k
        return ans