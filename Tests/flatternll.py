"""
                                    1
                                2        6
                            3          7    8
                        4       5   9   10

preOrder =>
root.val
root.left
root.right

[1,2,3,4,5,]

"""

class LLNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Node:

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None
        self.head = LLNode(0)
        #self.getLL(self)

    def getLLArr(self,root):
        
        arr = []
        if root: 
            arr.append(root.val)
            print(root.val)
            #arr.append(root.val)
            arr += self.getLLArr(root.left)
            arr += self.getLLArr(root.right)
        
        return arr
    
    def getLL(self):
        a = self.getLLArr(self)
        cur = self.head
        for i in a:
            cur.next = LLNode(i)
            cur = cur.next

        return self.head.next


c = Node(1)
c.left = Node(2)
c.left.left = Node(3)
c.left.left.left = Node(4)
c.left.left.right = Node(5)

c.right = Node(6)
c.right.left =Node(7)
c.right.right = Node(8)
c.right.left.right = Node(10)


head = c.head
a = c.getLL()

print("a",a)

        
