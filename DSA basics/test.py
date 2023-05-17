
"""
binary tree

                                    6
                            2               10
                        1       4         7     13
                              3    5

[6] d = l appendleft => left and right
[10,2] d = r appendleft => right and left
[13,7,4,1] d = l
[3,5] d = r
"""

from collections import deque
class Tree:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
    
    def add(self,val):
        node = self
        if node:
            if val < node.val:
                if node.left:
                    node.left.add(val)
                else:
                    node.left = Tree(val)
            if val > node.val:
                if node.right:
                    node.right.add(val)
                else:
                    node.right = Tree(val)

    def getInOrder(self):
        node = self
        arr = self.inOrder(node)
        print(arr)

    def getPreOrder(self):
        node = self
        arr = self.preOrder(node)
        print(arr)

    def getPostOrder(self):
        node = self
        arr = self.postOrder(node)
        print(arr)

    def inOrder(self,node):
        arr = []

        if node:
            arr += self.inOrder(node.left)
            arr.append(node.val)
            arr += self.inOrder(node.right)
        return arr

    def preOrder(self,node):
        arr = []

        if node:
            arr.append(node.val)
            arr += self.preOrder(node.left)
            
            arr += self.preOrder(node.right)
        return arr

    def postOrder(self,node):
        arr = []

        if node:
            
            arr += self.postOrder(node.left)
            
            arr += self.postOrder(node.right)
            arr.append(node.val)
        return arr

    def getSuccessor(self,val):

        successor = None
        root = self
        while root:
            if val < root.val:
                successor = root.val
                root = root.left
            elif val > root.val:
                root = root.right
            elif val == root.val:
                
                root = root.right
        
        return successor

    def maxDepth(self,root):
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

    def zigZagTraversal(self):
        q = deque()
        root = self
        if root:
            q.append(root)
        
        directionRight = True
        ans = []
        while q:
            
            child = deque()
            for n in list(q):
                i = q.popleft()
                ans.append(i.val)
                if directionRight == True:
                    if n.right:
                        child.appendleft(n.right)
                    if n.left:
                        child.appendleft(n.left)
                if directionRight == False:
                    if n.left:
                        child.appendleft(n.left)                    
                    if n.right:
                        child.appendleft(n.right)
            q = child
            if directionRight == False:
                directionRight = True
            else:
                directionRight = False

        return ans

c = Tree(6)
c.add(10)
c.add(2)
c.add(1)
c.add(13)
c.add(4)
c.add(5)
c.add(3)

c.add(7)
c.getInOrder()
c.getPreOrder()
c.getPostOrder()
print("successor",c.getSuccessor(5))
print(c.maxDepth(c))
print(c.zigZagTraversal())
