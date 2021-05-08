class Solution:
    def isSorted(self,arr,n):
        #code here
        inc=1
        d=1
        
        for i,e in enumerate(arr[:n-1]):
            if arr[i+1]>=arr[i]:
                continue
            else:
                inc=0
                break
        for i,e in enumerate(arr[:n-1]):
            if arr[i+1]<=arr[i]:
                continue
            else:
                d=0
                break
        
        if inc or d:
            return 1
        else:
            return 0
            
                
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ =='__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        print(Solution().isSorted(arr,n))
# } Driver Code Ends
