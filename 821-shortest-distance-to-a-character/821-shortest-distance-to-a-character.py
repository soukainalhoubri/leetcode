class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        n=len(s)
        ans=[]
        for slow in range(n):
            fast=0
            mindis=10**4+1
            while fast<n:
                if s[fast]==c:
                    mindis=min(mindis,abs(fast-slow))
                fast+=1
            ans.append(mindis)
                
        return ans