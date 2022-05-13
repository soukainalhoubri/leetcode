def longestCommonPrefix(self, strs):
        
        n=len(strs)
        if n==1:
            return strs[0]
        strs.sort()
        s=len(strs[0])
        ans=""
        for i in range(0,s):
            
            for j in strs:
                if(j[:i+1]!=strs[0][:i+1]):
                    return ans
                elif j[:i+1]==strs[0][:i+1] and j==strs[-1]:
                    ans=strs[0][:i+1]
        return ans