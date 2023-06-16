"""
-2, 1, -3, 4, -1, 2, 1, -5, 4
l

algorithm:-
calculate sum at each step
if sum < 0 then set 0
else 
add to cur sum
get max

"""

def getMaxSum(arr):
    maxSum = arr[0]
    curSum = 0
    for i in arr:
        if curSum < 0:
            curSum = 0
        
        curSum += i
        maxSum = max(maxSum,curSum)

    return maxSum
print(getMaxSum([1, -2, 3, 4, -1, 2, -5, 4]))

"""
"A man, a plan, a canal, Panama"
racecar
hello


"""

def isPalindrome(s):
    s = "".join([i.lower()  for i in s if i.isalnum()])
    print(s)
    l = 0
    r = len(s) -1
    while l <=r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True

s = "hello"
print(isPalindrome(s))
