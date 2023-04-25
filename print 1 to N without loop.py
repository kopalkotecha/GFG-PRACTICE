#Print 1 to N without loop in Python

class Solution:    
    #Complete this function
    def printNos(self,N):
        #Your code here
        if N == 0:
            return 
        self.printNos(N-1)  #recursive call that prints all numbers from 1 to N-1 before printing N
        print(N, end = " ")
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
