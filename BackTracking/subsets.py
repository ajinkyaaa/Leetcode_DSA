class Solution:
    def subsets(self, nums):

        self.result = []
        self.visited = []
        self.dfs(nums,[])
        return self.result

    def dfs(self,arr,path):
        self.result.append(path)
        if len(arr) == 0:
            return
        else:
            for i in range(len(arr)):
                self.dfs(arr[i+1:],path+ [arr[i]])
        

c = Solution()
print(c.subsets([1,2,3]))
"""
                1                               2                           3
            12      13                      12      23                 13       23
        123             123             123             123         123             123
    
    
"""