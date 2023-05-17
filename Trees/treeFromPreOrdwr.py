class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(bound=None):
            if not inorder or inorder[0] == bound:
                return None
            root = TreeNode(preorder.pop(0))
            root.left = helper(root.val)
            inorder.pop(0)
            root.right = helper(bound)
            return root
            
        return helper()