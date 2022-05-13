def longestPalindrome(s):
        n=len(s)
        if(n==1):
            return s[0]
        else:
            max,ans=1,s[0]
            for i in range(1,n):
                
                print("i iteration :", i)
                a,b,k,palindrome=0,0,1,True
                while(a!=-1 and b!=n-1 and palindrome and max!=n):
                    
                    a,b=int(i-k/2),int(i+k/2)
                    rev=s[a:b+1]
                    if(b-a % 2 ==1) and s[a]==s[b]:
                       k+=1
                       if(b-a+1>max):
                            max=b-a+1
                            ans=rev
                    
                    elif (b-a % 2 ==0) and (rev==rev[::-1]):
                        k+=1
                        if(b-a+1>max):
                            max=b-a+1
                            ans=rev
                    else:
                        palindrome=False
                    print("while iteration :", k)
                    print("max :",max)
                    print("answer :", ans)
                    print("a & b :",a,b)
                    print("palidrome", palindrome)
        return ans


print(longestPalindrome("abba"))