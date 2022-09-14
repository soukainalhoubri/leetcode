class Solution:
    def squre_sum(self,num):
            result=0
            for i in str(num):
                result+=int(i)**2
            return result
    def isHappy(self, n: int) -> bool:
        slow,fast=n,n
        while True:
            slow=self.squre_sum(slow)
            fast=self.squre_sum(self.squre_sum(fast))
            if slow==fast:
                break
        return slow==1
        