"""
s = "babad"
and "bab"

abad bacdca bacdcax abcddcba abxcddcyba

abcddcba # op = a
l

abcddcba # op = b
 l          l in case of odd

abcddcba # op = b
   l        in case of even
    l+1
"""

class Palindrome:
    def __init__(self,s):
        self.s = s
    
    def maxPalindrome(self):
        maxCount = 0
        for i in range(len(self.s)):
            count = self.helper(i,i)
            maxCount = max(maxCount,count)

            count = self.helper(i,i+1)
            maxCount = max(maxCount,count)
        
        return maxCount



    def helper(self,l,r):
        while l >= 0 and r <= len(self.s)-1 and self.s[l] == self.s[r]:
            l-=1
            r+=1
        return r-l-1

s = "abxcddcyba"
c = Palindrome(s)
print(c.maxPalindrome())