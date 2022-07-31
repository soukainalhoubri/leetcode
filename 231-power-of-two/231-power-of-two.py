class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if int(n)==0 or int(n)!=n:
            return False
        if n in(1,2):
            return True
        return self.isPowerOfTwo(n/2)