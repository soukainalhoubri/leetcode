def findLast(nums):
    n=len(nums)
    s=n//2
    k=0
    for i in range(n-1,0,-1):
        if(nums[i]<nums[i-1]):
            k=i
            while(k!=n-1 and nums[k]==nums[k+1]):
                k+=1
            return k
    
    return 0

def findFirst(nums):
    n=len(nums)
    s=n//2
    for i in range(s):
        if(nums[i]>nums[i-1]):
            return i
    return 1
           
def findUnsortedSubarray(nums):
        if(len(nums)==1):
            return 0
        else:
            a=findLast(nums)
            b=findFirst(nums)
            return a-b+1
           


print(findLast([2,2,2,1]))
print(findFirst([2,2,2,1]))
print(findUnsortedSubarray([2,2,2,1]))