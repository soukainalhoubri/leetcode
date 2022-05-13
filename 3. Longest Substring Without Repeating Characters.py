#Time limit exceeded :'(
# def check_repetition(s):
#         unique=set()
#         for i in s:
#             if i in unique:
#                 return False
#             else:
#                 unique.add(i)
#         return True


# def lengthOfLongestSubstring(self, s):
#         n=len(s)
#         if n==0:
#             return 0
#         for i in range(n,1,-1):
#             start=0
#             for k in range(n-i+1):
#                 string=s[start:start+i]
#                 if check_repetition(string):
#                     start+=1
#                 else: return i
            
            
        
        
#         return 1
# print(check_repetition("aaaa"))


def lengthOfLongestSubstring(s):
 start = maxLength = 0
 usedChar = {}
 for index,char in enumerate(s):
            if char in usedChar and start <= usedChar[char]:
                start = usedChar[char] + 1
            else:
                maxLength = max(maxLength, index - start + 1)
	usedChar[char] = index
 return maxLength