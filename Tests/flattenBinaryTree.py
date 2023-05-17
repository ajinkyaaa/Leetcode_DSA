"""
                                    1
                                2       5
                            3      4        6


123456

preOrder:-
traverse left node
get value
traverse right node

preOrder:-
get value
traverse left node
traverse right node
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Tree:
    def __init__(self,val):
        self.val= val
        self.left = None
        self.right = None
        self.arr = []

    def createLinkedList(self,root):
        ll = res =  Node(0)

        arr = self.flatten(root)
        for i in arr:
            ll.next = Node(i)
            ll = ll.next
        return res.next
    
    def flatten(self,root):
        if root is None:
            return
        
        self.arr.append(root.val)
        self.flatten(root.left)
        self.flatten(root.right)

        return self.arr


n = Tree(1)
n.left = Tree(2)
n.right = Tree(5)
n.left.left = Tree(3)
n.left.right = Tree(4)
n.right.right = Tree(6)


res = n.createLinkedList(n)
print("a")

