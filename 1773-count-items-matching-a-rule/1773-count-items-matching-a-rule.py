class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruletoindex={"type":0,"color":1,"name":2}
        k=ruletoindex.get(ruleKey)
        answer=0
        for i in items:
            if i[k]==ruleValue:
                answer+=1
        return answer