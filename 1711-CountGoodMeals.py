#time limit exceeded

# def check_power_of_two(number):
#     while number != 1:
#         if number % 2:
#             return False
#         number /= 2
#     return True
# def countPairs(deliciousness):
#         goodmeals=0
#         n=len(deliciousness)
#         if n==1:
#             return 0
#         else:
#             for i in range(n-1):
#                 for j in range(i+1,n):
#                     if check_power_of_two(deliciousness[i]+deliciousness[j]):
#                         goodmeals+=1
#             return goodmeals
           
# print(countPairs([1,3,5,7,9]))

#time limit exceeded
# def countPairs(self, deliciousness):
#    goodmeals=0
#    n=len(deliciousness)
#    if n==1:
#        return 0
#    else:
#        powers=[1]
#        for i in range(1,22):
#            powers.append(2*powers[i-1])
#        # powers={1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384}
#        for i in range(n-1):
#            for j in range(i+1,n):
#                if(deliciousness[i]+deliciousness[j]) in powers:
#                    goodmeals+=1
#        return goodmeals


#time limit exceeded :'(

def countPairs(deliciousness):
        goodmeals=0
        gm_found={}
        n=len(deliciousness)
        powers=[1]
        for i in range(1,22):
            powers.append(2*powers[i-1])
        if n==1:
            return 0
        else:
            for i in range(n-1):
                for j in range(i+1,n):
                    if (deliciousness[i],deliciousness[j])in gm_found and  gm_found[(deliciousness[i],deliciousness[j])]>=1:
                        
                        gm_found[(deliciousness[i],deliciousness[j])]+=1
                    elif (deliciousness[i],deliciousness[j]) in gm_found and gm_found[(deliciousness[i],deliciousness[j])]==-1:
                        continue
                    else:
                        if deliciousness[i]+deliciousness[j] in powers:
                            gm_found[(deliciousness[i],deliciousness[j])]=1
                        else:
                            gm_found[(deliciousness[i],deliciousness[j])]=-1
        
        for i in gm_found:
            if gm_found[i]>=1:
                goodmeals+=gm_found[i]
        return goodmeals%(10**9 + 7)

# print(countPairs([1,5]))



#I could've just iterated through the array of powers then search for the power-i in the dictionnary :)

# def countPairs(deliciousness):
#  powersoftwo=[2**i for i in range(22)]
 
   







