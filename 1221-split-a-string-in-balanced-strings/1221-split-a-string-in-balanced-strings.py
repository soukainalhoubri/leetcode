class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        n=len(s)
        answer=0
        k=s[0]
        stack=[]
        for i in range(n):
            if s[i]==k:
                stack.append(s[i])
            else:
                stack.pop()

            if len(stack)==0 and i!=n-1:
                answer+=1
                k=s[i+1]
        return answer+1
        
        