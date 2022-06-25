class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        if len(needle)==len(haystack):
            if needle==haystack:
                return 0
            return -1
        if needle not in haystack:
            return -1
        n,m=len(haystack),len(needle)
        for i in range(n-m+1):
            if haystack[i:i+m]==needle:
                return i
        
        