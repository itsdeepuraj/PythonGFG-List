# Function to calculate average
def calc_average(arr):
    # Your code here
    max_v = max(arr)
    min_v = min(arr)
    
    Sum = sum(arr) - max_v - min_v
    Len = len(arr)-2
    average = Sum//Len
    return average

#{ 
#  Driver Code Starts
#Initial Template for Python 3


# Driver Code
if __name__ == '__main__':
    # Testcase input
    testcases = int(input())
    # Looping through testcases
    while(testcases > 0):
        N = int(input())
        
        a = list(map(int,input().strip().split()))
        
        print (calc_average(a))
        
        testcases -= 1
# } Driver Code Ends
