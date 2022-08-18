import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        #[3,3,3,3,5,5,5,2,2,7]
        #count occurences of every integer in the array, put in a hashmap
        #summing minim couts until I reach half length of the array
        #{3:4,5:3,2:2,7:1}
        #5
        #4+3
        #O(N)+O(N)=O(N): Time complexity
        #space complexity: O(N)
        n=(len(arr)//2)+len(arr)%2
        counts={i:0 for i in arr}
        for num in arr:
            counts[num]+=1
        _sum=0
        heap=[counts[i] for i in counts]
        array=heapq.nlargest(n,heap)
        index=0
        while _sum<n:
            _sum+=array[index]
            index+=1
        return index