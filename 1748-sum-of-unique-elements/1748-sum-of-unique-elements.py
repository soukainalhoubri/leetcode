class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        occurences={}
        for i in nums:
            if occurences.get(i):
                occurences[i]+=1
            else:
                occurences[i]=1
                
        Sum=0
        for i in occurences:
            if occurences.get(i)==1:
                Sum+=i
        return Sum