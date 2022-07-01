class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #I should keep track of the array of minimal length
        #If I sort the array it would make it easier for me, as I can return the answer in any order
        #let's try the intuitive method where I iterate over the array of minimal length and then check if the item is present in the onger array, then I store it
        counts1={}
        for i in nums1:
            if i in counts1:
                counts1[i]+=1
            else:
                counts1[i]=1
        counts2={}
        for i in nums2:
            if i in counts2:
                counts2[i]+=1
            else:
                counts2[i]=1
        ans=[]
        for i in counts1:
            if i in counts2:
                ans.extend([i]*min(counts1[i],counts2[i]))
        return ans
        