#Palindrome in Python

class Solution:
	def is_palindrome(self, n):
		# Code here
		string = str(n)
		
		if string == string[::-1]:
            return "Yes"
        elif len(set(string)) <= 1:
            return "Yes"
        else:
            return "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
# } Driver Code Ends
