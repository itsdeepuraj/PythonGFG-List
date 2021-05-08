class Solution:
    
    
    def insertAtIndex(self, arr, sizeOfArray, index, element):
        arr.insert(index,element)
        return
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():
    T=int(input())
    while(T>0):
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        arr.append(-1)
        index,element=map(int,input().strip().split())
        
        Solution().insertAtIndex(arr,sizeOfArray,index,element)
        
        for i in range(sizeOfArray):
            print(arr[i],end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
