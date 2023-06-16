class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ""
        dic = {b:a+1 for a,b in enumerate("abcdefghijklmnopqrstuvwxyz")}
        print(dic)
        cur = ""
        for c in s:
            cur += str(dic[c])
        
        add = 0
        while k >0:
            for c in cur:
                add += int(c)
            cur = str(add)
            k -=1
        print(cur)
s = Solution()
s.getLucky("leetcode",2)