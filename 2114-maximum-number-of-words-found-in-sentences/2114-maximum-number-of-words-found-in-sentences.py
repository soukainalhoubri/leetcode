class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        Maxwords=0
        for i in sentences:
            Maxwords=max(Maxwords,len(i.split(" ")))
        return Maxwords