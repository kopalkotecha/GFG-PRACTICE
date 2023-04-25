#Alternate Elements of an Array in Python

# arr is the array
# n is the number of elements in array
def printAl(arr,n):
    # your code here
    for i in range(n):
        if i%2 == 0:                     #if index is even it'll print alternate elements
            print (arr[i],end=' ')       #end=' ' to ensure that the next element is printed on the same line.


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        printAl(arr,n)
        print()
# } Driver Code Ends

