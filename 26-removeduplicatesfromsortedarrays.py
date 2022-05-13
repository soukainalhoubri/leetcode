def removeDuplicates(nums):
        n=len(nums)
        if(n==1):
            return 1
        for i in range(n-1):
            if(nums[i]==nums[i+1]):
                nums=nums[:i]+nums[i+1:]
                n-=1
        return len(nums)
       

print(removeDuplicates([1,1,2]))