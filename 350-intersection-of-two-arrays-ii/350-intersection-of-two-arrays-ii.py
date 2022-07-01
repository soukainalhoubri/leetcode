class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #this is the bruteforce way
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
        
#time complexity:

#let n=len(nums1) and m=len(nums2)
#T= O(n+m)

#space complexity:

# in counts, we might store all of the items of both the arrays
#so we surely have O(n+m)
#and we will also store the answer array which will be of length min(n,m) in the worst case, which is still O(n+m) 
