# Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

# Sample Input:
# [3 4 1 4 1]

# Sample Output:
# 1

# If there are multiple possible answers ( like in the sample case above ), output any one.
# If there is no duplicate, output -1

def findDupsInArray(A):
    n = len(A)
    if(n == 1):
        return -1
    B = [0]*n
    for i in A:
        if(B[i-1] == 0):
            B[i-1] = 1
        else:
            return i
    return -1
A = [1,2,3,1,2,3,1,2,3,4]
print(findDupsInArray(A))