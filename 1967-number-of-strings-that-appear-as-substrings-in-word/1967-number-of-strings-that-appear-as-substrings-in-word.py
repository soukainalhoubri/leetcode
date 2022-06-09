class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        answer=0
        for i in patterns:
            if word.find(i)!=-1:
                answer+=1
        return answer