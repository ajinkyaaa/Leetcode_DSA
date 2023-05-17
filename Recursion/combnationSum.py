
class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], res)
        print(res)
        return res

    def backtrack(self, candidates, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(candidates)):
            self.backtrack(candidates, target-candidates[i], i, path+[candidates[i]], res)

s = Solution()
print(s.combinationSum([1,2,3],5))

"""
#Steps:-

sort array
use backtrack, if target less than 0 then backtrack
if 0 then append to result
else iterate each element and backtrack while decrementing target

"""