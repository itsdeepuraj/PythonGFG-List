def reverseArray(arr,n):
    
    #code here
    s = 0
    e = len(arr)-1
    while s<e:
        arr[s], arr[e] = arr[e], arr[s]
        s = s + 1
        e = e - 1
        
    return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        reverseArray(arr,n)
        
        for e in arr:
            print(e,end=' ')
        print()
# } Driver Code Ends
