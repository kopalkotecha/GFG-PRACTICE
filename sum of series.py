#Sum of Series (1+2+3+....) in Python

class Solution:
    
	def seriesSum(self,n):
	    # code here
	    return int(n*(n+1)/2)    //use the direct formula for the series

#{ 
 # Driver Code Starts
                               #Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.seriesSum(n)
        print(ans)
        tc=tc-1
# } Driver Code Ends
