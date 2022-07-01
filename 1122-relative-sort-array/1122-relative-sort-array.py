class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts={}
        for i in arr1:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
        ans=[]
        for i in arr2:
            ans.extend([i]*counts[i])
            del counts[i]
        while counts:
            m=min(counts)
            ans.extend([m]*counts[m])
            del counts[m]
        return ans