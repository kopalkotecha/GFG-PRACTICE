#Find the Median in Python

class Solution:
	def find_median(self, v):
		# Code here
		v.sort()
		if len(v) % 2 != 0:
		    left = 0
		    right = len(v)
		    mid = (left+right)//2
		    return v[mid]
		else:
		    left = 0
		    right = (len(v)//2)
		    mid = (v[right]+v[right-1])//2   #-1 because indexing starts from 0
		    return mid

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends
