def sumOddLengthSubarrays(self, arr):
        n=len(arr)
        somme=0
        for i in range(1,n+1,2):
            k=0
            while(k+i<=n):
                somme+=sum(arr[k:k+i])
                k+=1
        return somme