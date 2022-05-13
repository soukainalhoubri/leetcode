def maxOperations(nums, k):
        used_numbers={}
        operations=0
        for i in nums:
            if(k-i in used_numbers and used_numbers[k-i]>0):
                operations+=1
                used_numbers[k-i]-=1
            elif(i not in used_numbers):
                used_numbers[i]=1
            else:
                used_numbers[i]+=1
        return operations
print(maxOperations([1,2,3,4,3],6))

