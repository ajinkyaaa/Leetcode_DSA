from collections import defaultdict
class Solution:
    def characterReplacement(self, s, k) -> int:
        count = defaultdict(int)
        res = 0
        l = 0
        maxFreq = 0
        for r,wrd in enumerate(s):
            count[s[r]]+=1
            maxFreq = max(maxFreq, count[s[r]])
            
            while (r - l + 1) - maxFreq > k:
                  count[s[l]]-=1
                  l+=1
            res = max(res, r - l + 1)
        return res

s = Solution()
print(s.characterReplacement("AABABBAAAA",2))

"""
for each loop get max Frequency
keep on increasing the window and check if difference of max freq is greater than k,if yes then decrement count of s[l] character and slide l to right
calculate max window size
"""