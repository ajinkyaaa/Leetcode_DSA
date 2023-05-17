class Solution:
    def rob(self, nums) -> int:
        memo=[-1 for _ in range(len(nums))]
        def dp(i):
            if i<0:
                return 0 
            elif memo[i]>=0:
                return  memo[i]
            else:
                res=max(dp(i-2)+nums[i],dp(i-1))
                memo[i]=res
                return res
        return dp(len(nums)-1)