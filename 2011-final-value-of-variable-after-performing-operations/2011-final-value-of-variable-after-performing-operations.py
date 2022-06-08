class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer=0
        for i in operations:
            if i[1]=="-":
                answer-=1
            else:
                answer+=1
        return answer