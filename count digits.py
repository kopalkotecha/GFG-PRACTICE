#Count Digits in Python


class Solution:
    def evenlyDivides (self, N):
        # code here
        num = 0
        for i in str(N):
            if i != "0" and N % int(i) == 0:
                num += 1
        return num
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends
