def maximumElement(arr,n,):
    #return required result
    
    #code here
    if not arr:
        return None
        
    else:
        res = arr[0]
        for i in range(1, len(arr)):
            if arr[i]>res:
                res= arr[i]
    return res


def minimumElement(arr,n):
    #return required result
    
    #code here
    if not arr:
        return None
        
    else:
        res = arr[0]
        for i in range(1, len(arr)):
            if arr[i]<res:
                res= arr[i]
    return res

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
        
        max=maximumElement(arr,n,)
        min=minimumElement(arr,n)
        print(max,min)
# } Driver Code Ends
