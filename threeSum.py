class Solution:
    def threeSum(self, nums):
        nums.sort()
        l = 0
        r = len(nums)-1
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -=1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans
        

"""
sort the list
if sum of next and last > target, reduce r else increment l
else append and increment l
"""