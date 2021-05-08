class Solution:
    ##Complete the below codes
    #Function to find median of the array elements.
    def median(self,A,N):
        
        A.sort()
        N = len(A)
        if N%2==0:
            median1 = A[N//2]
            median2 = A[N//2 - 1]
            median  = (median1 + median2)//2
            
        else:
            median = A[N//2]
            
        return median
        
        ##Your code here
        
        #If median is fraction then convert the median to integer and return
     
    #Function to find mean of the array elements.   
    def mean(self,A,N):
        ##Your code here
        N = len(A)
        sum = 0
        for x in A:
            sum = sum + x
            
        return (sum//N)

#{ 
#Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.mean(a,N),ob.median(a,N))
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends
