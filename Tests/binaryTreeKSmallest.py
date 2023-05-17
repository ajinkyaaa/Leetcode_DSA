"""
                                    10
                            (1)  5             15
                            (0)1   (2) 7    12   18
k = 1

inorder =:
1=>5 =>7 =>12 =>15 => 18=>10

1 =>k = 0
5 => k= 1
7 => k = 2

"""

class BinaryTree:
    def __init__(self,val):
        self.val = val
        self.left= None
        self.right = None
        self.res = None
        self.k = None

    def getKSmallest(self,k):
        root = self
        self.k = k
        
        #arr = self.inOrderTraversal(root,k)
        self.dfs(root)
        return self.res


    def inOrderTraversal(self,root):
        arr = []
        if root:
            arr += self.inOrderTraversal(root.left,self.k)
            arr.append(root.val)
            arr += self.inOrderTraversal(root.right,self.k)
        
        return arr

    def dfs(self,root):
        if root is None:
            return
        if self.res:
            return
        if self.left:
            self.dfs(root.left)
        self.k = self.k - 1
        if self.k == 0:
            self.res = root.val
        
        if root.right:
            self.dfs(root.right)
        
        


c = BinaryTree(10)
c.left = BinaryTree(5)
c.left.left = BinaryTree(1)
c.left.right = BinaryTree(7)

c.right = BinaryTree(15)
c.right.right = BinaryTree(18)
c.right.left = BinaryTree(12)
print(c.getKSmallest(4))

