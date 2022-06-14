class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        n=len(s)
        ans=[]
        ind=set()
        for i in range(n):
            if s[i]==c:
                ind.add(i)
        for i in range(n):
            ans.append(min(abs(i-k) for k in ind))
            
        return ans
#         for slow in range(n):
#             fast=0
#             mindis=10**4+1
#             while fast<n:
#                 if s[fast]==c:
#                     mindis=min(mindis,abs(fast-slow))
#                 fast+=1
#             ans.append(mindis)
                
#         return ans
    