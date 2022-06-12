class Solution:
    def digitCount(self, num: str) -> bool:
        n=len(num)
        counts={i:0 for i in range(10)}
        for i in num:
            counts[int(i)]+=1
        for i in range(n):
            if int(num[i])!=counts[i]:
                return False
        return True