#Reverse Digits in Python

class Solution:
	def reverse_digit(self, n):
		# Code here
		string = str(n)
		reverse = ''
		
		for i in string[::-1]:
		    reverse += i
		return int(reverse)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends
