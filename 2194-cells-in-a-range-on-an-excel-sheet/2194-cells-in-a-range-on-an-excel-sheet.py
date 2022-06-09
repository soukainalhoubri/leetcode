class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        n=int(s[1])
        m=int(s[-1])
        k=ord(s[0])
        p=ord(s[-2])
        answer=[]
        for j in range(k,p+1):
            for i in range(n,m+1):
                answer.append(chr(j)+str(i))
        return answer