class Solution:
    def firstUniqChar(self, s: str) -> int:
        #iterate over the array once to get counts, store them in a hashmap
        #iterate once again, return the first element with count=1
        #else return -1
        #time O(N)
        #space O(N)
        counts={c:0 for c in s}
        for c in s:
            counts[c]+=1
        for i,c in enumerate(s):
            if counts[c]==1:
                return i
        return -1
            
        