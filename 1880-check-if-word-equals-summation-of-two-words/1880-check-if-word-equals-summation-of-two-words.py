class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        numerical={chr(i):i-97 for i in range(97,107)}
        
        def get_numerical(s):
            ans=""
            for i in s:
                ans+=str(numerical[i])
            return ans
        
        s1=get_numerical(firstWord)
        s2=get_numerical(secondWord)
        s3=get_numerical(targetWord)
        
        return int(s1)+int(s2)==int(s3)