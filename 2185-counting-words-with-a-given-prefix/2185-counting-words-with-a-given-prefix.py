class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        answer=0
        n=len(pref)
        for word in words:
            if len(word)>=n and word[:n]==pref:
                answer+=1
                
        return answer