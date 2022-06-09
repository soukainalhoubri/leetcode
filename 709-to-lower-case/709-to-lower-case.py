class Solution:
    def toLowerCase(self, s: str) -> str:
        for i in s:
            if ord(i)<=90 and ord(i)>=65:
                s=s.replace(i,chr(ord(i)+32),1)
        return s