from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dicS = defaultdict(int)
        dicT = defaultdict(int)
        need = 0
        have = 0
        for c in t:
            dicT[c] += 1
            need += 1

        #dicT = {A:1,B1,C1} and need = 3
        l = 0
        minLength = float("inf")
        for r in range(len(s)):
            dicS[s[r]] += 1
            if s[r] in dicT and dicT[s[r]] >= dicS[s[r]]:
                have +=1

                while have == need:
                    minLength = min(minLength,r-l+1)
                    print(s[l:r+1])
                    dicS[s[l]] -=1 
                    if s[l] in dicT and dicS[s[l]] < dicT[s[l]]:
                        have -=1
                    l+=1
                
                while l < r and s[l] not in dicT:
                    l +=1
        return minLength

c = Solution()
print(c.minWindow("ADOBECODEBANC","AB"))

"""
s =ADOBECODEBANC
t =ABC
dicT = {
    a:1
    b:1
    c:1   
}
dicS ={
    a:1
    b:1
    c:1
    D,O,E
}
need = 3 have 0

A   D   O   B   E   C   O   D   E   B   A   N   C   
            l
                                        r

dicS[r] += 1
if r in dicT and dics[r] == dicT[r]:
    have +=1

while have == need
    dic[l]-1
    
    if l in dicT:
        have -=1
    l+=1

while l not in dicT:
    l+1











"""