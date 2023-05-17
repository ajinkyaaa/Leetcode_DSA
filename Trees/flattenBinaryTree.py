# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = self.preOrderTraversal(root)
        ans = root
        for i in arr[1:]:
            if root is not None:
                root.left = None
                root.right = TreeNode(i)
                root = root.right
        print(ans.right.right.val)
        
    def preOrderTraversal(self,root):
        arr = []
        if root is not None:
            arr.append(root.val)
            arr += self.preOrderTraversal(root.left)
            arr += self.preOrderTraversal(root.right)
        
        return arr

c = TreeNode(1)
c.left =  TreeNode(2)
c.right =  TreeNode(3)

n = Solution()
n.flatten(c)