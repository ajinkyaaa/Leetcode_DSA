"""
                                        1
                                    2       3
                                4     5         6
                            7

[1,3,6,7]

q:-
[1]
[2,3]
[4,5,6]
[7]

"""

from collections import deque
class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def rightSideViw(self):
        root = self
        q = deque()
        result = []
        if root:
            q.append(root)
            result.append(root.val)

        while q:
            
            child = deque()
            for i in range(len(q)):
                n = q.popleft()
                
                if n.left:
                    child.append(n.left)
                if n.right:
                    child.append(n.right)
            if child:
                result.append(child[-1].val)
                q = child

        return result

c = Tree(1)
c.left = Tree(2)
c.right = Tree(3)
c.left.left = Tree(4)
c.left.right = Tree(5)
c.left.left.left = Tree(7)
c.right = Tree(3)
c.right.right = Tree(6)
            
ans = c.rightSideViw()
print(ans)



