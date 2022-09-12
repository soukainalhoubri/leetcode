class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        # for k in range(1,n+1):
        #     max_sum=float('-inf')
        #     current_sum=0
        #     for i in range(n):
        #         current_sum+=nums[i]
        #         if i>=k:
        #             current_sum-=nums[i-k]
        #         max_sum=max(max_sum,current_sum)
        #         if max_sum>=target:
        #             return k
        # return 0
        
        #we will find a window that sums up to target
        
#         for i in nums:
#             current_sum+=i
#             min_length=min(min_length,i+1)
#             if current_sum>=target:
#                 break
        
#         if min_length<float('inf'):
#             c=min_length
#             start=0
#             while c<n and start<n:
#                 if current_sum>=target:
#                     current_sum-=nums[start]
#                     start+=1
#                 else:
#                     current_sum+=nums[c]
#                     c+=1
#                     min_length=min(min_length,c-start+1)
#             return min_length

        min_length=float('inf')
        current_sum=0
        start=0
        for end in range(n):
            current_sum+=nums[end]
            while current_sum>=target:
                min_length=min(min_length,end-start+1)
                current_sum-=nums[start]
                start+=1
            
            
        if min_length<float(inf):
            return min_length
            
        return 0
        
        