class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n=len(word)
        a=n+1
        for i in range(n):
            if word[i]==ch:
                a=i
                break
        if a!=n+1:
            return word[:a+1][::-1]+word[a+1:]
        return word
                
            
            