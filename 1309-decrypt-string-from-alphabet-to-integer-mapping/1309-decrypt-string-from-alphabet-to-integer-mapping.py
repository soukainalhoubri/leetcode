class Solution:
    def freqAlphabets(self, s: str) -> str:
        hashing={str(i):chr(97+i-1) for i in range(1,10)}
        hashing1={str(i)+"#":chr(97+i-1) for i in range(10,27)}
        for i in hashing1:
            s=s.replace(i,hashing1.get(i))
            
        for i in hashing:
            print(i,hashing[i])
            s=s.replace(i,hashing.get(i))
        return s