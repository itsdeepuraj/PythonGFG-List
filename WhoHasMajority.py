class Solution:
    #Function to find element with more appearances between two elements in an array.    
    def majorityWins(self, arr, n, x, y):
        # code here
        def majorityWins(self, arr, n, x, y):
            count_x=0;
            count_y=0;
        
            for i in range(0,n):
                #Iterating through the array elements.
                #Incrementing the counter variables accordingly.
                if(arr[i]==x):
                    count_x+=1
                if(arr[i]==y):
                    count_y+=1
            
            #Comparing the two counters.
            #If both appear same number of times, returning the smaller number.
            if(count_x>count_y or (count_x==count_y and x<y)):
                #Returning the number with more appearances in the array.
                return x
            else:
                #Returning the number with more appearances in the array.
                return y
#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        x,y=map(int,input().strip().split())
        
        print(Solution().majorityWins(arr,n,x,y))
        T-=1

# } Driver Code Ends
