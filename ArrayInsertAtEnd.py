def insertAtEnd(arr,sizeOfArray,element):
    ##Your code here
    arr.append(element)
    return


#{ 
#Driver Code Starts.


def main():
    testcases=int(input())
    
    while(testcases>0):
        sizeOfArray=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        
        element=int(input())
        
        insertAtEnd(arr,sizeOfArray,element)
        
        for i in arr:
            print(i,end=" ")
        print()
        
        testcases-=1
    

if __name__=="__main__":
    main()
#} Driver Code Ends
