class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #I should create a hashtable to contain the citizens who trust the judge
        #if it the citizen trusts someone else, they should be removed from  the hashtable
        #we test the condidates, we return the element which is trusted by n-1
        #if there is no element which is trusted by n-1, we return -1
        
        trust_count={i:0 for i in range(1,n+1)}
        for i in trust:
            trust_count[i[0]]=-1# the judge trusts no one
            if trust_count[i[1]]!=-1:
                trust_count[i[1]]+=1
        
        for i in trust_count:
            if trust_count[i]==n-1:
                return i
        return -1
    #let n=len(trust)
    #time_compleity: T=O(n)
    #space_complexity: S=O(n)oik;