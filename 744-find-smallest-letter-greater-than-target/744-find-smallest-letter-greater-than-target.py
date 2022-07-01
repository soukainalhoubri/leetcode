class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target>=letters[-1]:
            return letters[0]
        ans=letters[-1]
        for i in letters:
            if i>target and i<ans:
                ans=i
        return ans
                
        