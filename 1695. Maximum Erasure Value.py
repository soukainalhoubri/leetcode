def maximumUniqueSubarray(nums):
        seen = dict()
        ans = sum = 0
        l = 0
        for r, x in enumerate(nums):
            if x in seen:
                index = seen[x]
                while l <= index:  # Move the left side until index + 1
                    del seen[nums[l]]
                    sum -= nums[l]
                    l += 1

            seen[x] = r
            sum += x
            ans = max(ans, sum)
        return ans
       
print(maximumUniqueSubarray([1,2,3,8,3]))
