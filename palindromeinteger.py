'''Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.'''

#difficulty:easy

def isPalindrome(x):
    s=str(x)
    for i in range(len(s)):
        if(s[i]!=s[len(s)-i-1]):
            return False
        
    return True

