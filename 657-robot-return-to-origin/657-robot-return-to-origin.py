class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u=0
        l=0
        for i in moves:
            if i=='U':
                u+=1
            elif i=='D':
                u-=1
            elif i=='L':
                l+=1
            else:
                l-=1
        return u==0 and l==0