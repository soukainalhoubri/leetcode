class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n=len(s)
        answer=["x"]*n
        j=0
        for i in indices:
            answer[i]=s[j]  
            j+=1
        return ''.join(answer)