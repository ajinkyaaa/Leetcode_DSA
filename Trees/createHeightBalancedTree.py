
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        m = len(nums)//2
        root = TreeNode(nums[m])
        leftN = rightN = root

        l = nums[:m]
        r = nums[m+1:]
        
        while l:
            val = l[0]
            if leftN.val == nums[m]:
                leftN.left = TreeNode(val)
                leftN = leftN.left
            else:
                leftN.right = TreeNode(val)
                leftN = leftN.right
           
            l = l[1:]
            
        while r:
            val = r[0]
            if rightN.val == nums[m]:
                rightN.right = TreeNode(val)
                rightN = rightN.right
            else:
                rightN.right = TreeNode(val)
                rightN = rightN.right
      
            r = r[1:]      
        
        return root

c = Solution()
arr = [-10,-3,0,5,9]
c.sortedArrayToBST(arr)