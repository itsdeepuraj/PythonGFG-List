def deleteFromArray(arr,n,idx):
    for i in range(idx,n-1):
        arr[i] = arr[i+1]
    arr[n-1] = 0
    return

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#CONTRIBUTED BY RavinderSinghPB
if __name__ == '__main__':
    tcs= int(input())
    
    for _ in range(tcs):
        n=int(input())
        idx=int(input())
        
        arr=[i+1 for i in range(n)]
        
        deleteFromArray(arr,n,idx)
        
        for e in arr:
            print(e,end=' ')
        print()
        
# } Driver Code Ends
