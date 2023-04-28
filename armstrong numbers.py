#Armstrong Numbers in Python

class Solution:
    def armstrongNumber (ob, n):
        # code here 
        n = str(n)
        sum = 0
        for i in n:
            temp = int(i)
            sum += (temp) ** 3
            
        if (sum == int(n)):
            return "Yes"
        else:
            return "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends
