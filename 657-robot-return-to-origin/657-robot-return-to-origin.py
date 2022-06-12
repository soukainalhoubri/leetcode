class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counts={'U':0,'D':0,'L':0,'R':0}
        for i in moves:
            counts[i]+=1
        return counts.get('U')==counts.get('D') and counts.get('R')==counts.get('L')