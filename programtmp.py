
from collections import defaultdict
def characterReplace(wrd,k):
    dic = defaultdict(int)
    result = 0
    maxFreq = 0
    l = 0
    for r,char in enumerate(wrd):
        dic[wrd[r]] +=1
        maxFreq = max(maxFreq,dic[wrd[r]])
        while r-l+1 - maxFreq > k:
            dic[wrd[l]] -= 1
            l += 1
        result = max(r-l+1,result)
    return result

print(characterReplace("AABABBAAAA",2))


"""
A A B A B B A A A A 

          !
  !
"""

for i in range(0,5):
    print(i*2)