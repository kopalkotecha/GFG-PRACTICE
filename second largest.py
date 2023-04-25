#Second Largest in Python

class Solution:

	def print2largest(self,arr, n):
		# code here
		if n < 2:
            return -1
        first_largest, second_largest = arr[0], -1 
        for i in arr[1:]:
            if i > first_largest:
                second_largest = first_largest
                first_largest = i
            elif i > second_largest and i != first_largest:
                second_largest = i
        return second_largest

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
