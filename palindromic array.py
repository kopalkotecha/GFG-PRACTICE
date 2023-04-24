#Palindromic Array in Python

#Approach 1:
def ifPalin(n):
    string=str(n)
    reverse = string[::-1]
    if string == reverse:
        return 1
    return 0

def PalinArray(arr ,n):
    # Code here
    for i in range(n):
        if  ifPalin(arr[i]):
            continue
        else:
            return 0
    return 1


#Approach 2:
def PalinArray(arr ,n):
    # Code here
    for i in range(n):
        if str(arr[i])!=str(arr[i])[::-1]:  #checks if ith element of 'arr' list is not equal to its reverse
            return 0
    return 1
  
 '''
        if str(arr[i])!=str(arr[i])[::-1]: 
        - str() converts arr[i] into string then compares it to its reversed version.
        - checks if the ith element of 'arr' list is not equal to its reverse.
        - [::-1] = slicing syntax
 '''
