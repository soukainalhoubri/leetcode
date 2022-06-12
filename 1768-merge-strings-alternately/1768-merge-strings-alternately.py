class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m=len(word1),len(word2)
        ans=""
        x=min(n,m)
        last=0
        for i in range(x):
            ans+=word1[i]+word2[i]
            last=i
        if last!=n-1:
            ans+=word1[last+1:]
        elif last!=m-1:
            ans+=word2[last+1:]
        
        return ans