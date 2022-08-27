class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first={c:words[0].count(c) for c in words[0]}
        print(first)
        answer=[]
        for c in first:
            common=True
            minCount=first[c]
            for word in words:
                if c not in word:
                    common=False
                    print("word",word,' char ',c)
                    break
                else:
                    minCount=min(minCount,word.count(c))
            if common:
                answer.extend([c]*minCount)
        return answer
            
            