class Solution:
    def zigzagLevelOrder(self,root):
        res = []
        q = deque()
        if root:
            q.append(root)
        directionLeftToRight = False
        while q:
            val = []
            childNodes = deque()
            for i in range(len(q)):
                if directionLeftToRight == True:
                    node = q.popleft()
                    val.append(node.val)
                    if node.left:
                        childNodes.appendleft(node.left)
                    if node.right:
                        childNodes.appendleft(node.right)



                else:
                    node = q.popleft()
                    val.append(node.val)
                    if node.right:
                        childNodes.appendleft(node.right) 
                    if node.left:
                        childNodes.appendleft(node.left)    

            
            q = childNodes
            directionLeftToRight = False if directionLeftToRight else True
            res.append(val)
        
        return res

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

n = Node("A")
n.left = Node("B")
n.right = Node("C")
n.right.right = Node("D")
n.right.left = Node("E")
c = Solution()
print(c.zigzagLevelOrder(n))