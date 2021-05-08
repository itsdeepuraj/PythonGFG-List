class Solution:
    # inf has been imported in driver code
    def immediateGreater(self,arr,n,x):
        #return required ans
        
        #code here
        ans=-1
        diff = 10000000
        for e in arr:
            if e>x and e-x < diff:
                ans=e
                diff = e-x
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    from math import inf
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(e) for e in input().split()]
        x=int(input())
        
        ans=Solution().immediateGreater(arr,n,x)
        print(ans)
# } Driver Code Ends
