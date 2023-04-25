#Sum of Array Elements in Python

def sumElement(arr,n):
    #code here
    sum = 0
    for i in range(n):
        sum = sum + arr[i]
    return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    testCase=int(input())
    
    for _ in range(testCase):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        print(sumElement(arr,n))
# } Driver Code Ends
