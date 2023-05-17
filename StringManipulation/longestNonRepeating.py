from collections import defaultdict
def lengthOfLongestSubstring(s: str) -> int:
    coll = defaultdict(str)
    left = 0
    max_len = 0
    for r in range(len(s)):
        if s[r] in coll and left <= coll[s[r]]:
            left = coll[s[r]] + 1
        max_len = max(max_len,r-left+1)
        coll[s[r]] = r
        

        
    return max_len

print(lengthOfLongestSubstring("abcabcdab"))