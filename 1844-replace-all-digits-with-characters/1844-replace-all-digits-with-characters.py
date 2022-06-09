class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(x,n):
            return chr(ord(x)+n)
        
        n=len(s)
        for i in range(1,n,2):
            k=int(s[i])
            a=shift(s[i-1],k)
            s=s.replace(s[i],a,1)
        return s

            