class Solution:
    def sortSentence(self, s: str) -> str:
        
        words=s.split(" ")
        answer=['']*len(words)
        for i in words:
            k=int(i[-1])-1
            answer[k]=i[:-1]
        return ' '.join(answer)