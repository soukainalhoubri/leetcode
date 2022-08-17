def morse_code(word):
    morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    answer=''
    for char in word:
        answer+=morse[ord(char)-97]
        
    return answer
    
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        different = set()
        for word in words:
            different.add(morse_code(word))
        print(different)
        return len(different)