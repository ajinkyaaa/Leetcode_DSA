"""
                        1
                    2       3
                4    5    null    7

task:-
[1,#,2,3,#,4,5,#,7,#]

queue:-
[1]
[2,3]
[4,5,null,7]

if end of q append #
if null append #
"""

from collections import deque
class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    def rightPointer(self):
        result = []
        root = self
        q = deque()
        if root:
            q.append(root)
        
        while q:
            
            child = deque()

            for i in range(len(q)):
                n = q.pop()
                if n:
                    result.append(n.val)
           
                if n and n.left:
                    child.appendleft(n.left)
                if n and n.right:
                    child.appendleft(n.right)

            result.append("#")
            q = child
        
        return result

c = Tree(1)
c.left = Tree(2)
c.right = Tree(3)
c.left.left = Tree(4)
c.left.right = Tree(5)
c.right = Tree(3)
c.right.left = None
c.right.right = Tree(7)

a = c.rightPointer()
print(a)





