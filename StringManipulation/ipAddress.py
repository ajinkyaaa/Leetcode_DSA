class Solution:
    def restoreIpAddresses(self, s: str) :
        res = []
        def dfs(s,path,curCnt,num):
            if path and (path[-1] == "" or int(path[-1])>255):
                return
            if s == "":
                if ".".join(path) not in res  and len(path) == 4:
                    res.append(".".join(path))
            if num == "" or curCnt == 0  or int(num) > 255 or (len(s)-1) / curCnt >3:
                return

            else:
                for i in range(1,4):
                    if s[0] == "0" and i >1:continue
                    dfs(s[i:],path + [s[:i]],curCnt-1,s[:i])
            
                      

            
        dfs(s,[],4,s[0])
        print(res)

c = Solution()
print(c.restoreIpAddresses("0000"))

"""
Algorithm:
25525511135 

s = 5525511135 
num = 2

s = 2.552
num = 2511135 
--------------

num = 255
s = 25511135

num = 255.255
s = 11135

num = 255.255.11



"""