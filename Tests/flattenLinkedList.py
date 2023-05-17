"""
1  2    3   11  12  13
        4   5   9   10
            6   7   8

use case:-
if null then insert val null
front and back pointers

stack [1]
[2]
[11,4]
[11,5]
[11,9,6]
[11,9,7]
[11,9,8]
[11,10]
[12]
[13]

"""

from collections import deque
class Node:
    def __init__(self,val):
        self.next = None
        self.prev = None
        self.child = None
        self.val = val

class flattenLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def flatten(self):
        q = deque()
        dummy = res = Node(0)
        cur  =  self.head
        if cur:
            q.append(cur)
        
        while q:
            n = q.pop()
            print(n.val)
            if n.next:
                q.append(n.next)
            if n.child:
                q.append(n.child)

            dummy.next = n
            n.prev = dummy
            dummy.child = None
            dummy = dummy.next
        res.next.prev = None

        return dummy.next

c = flattenLinkedList()
c.head = Node(1)
c.head.next = Node(2)
c.head.next.next = Node(3)
c.head.next.next.next = Node(11)
c.head.next.next.child = Node(4)
c.head.next.next.child.next = Node(5)
c.head.next.next.child.next.next = Node(9)
c.head.next.next.child.next.child = Node(6)
c.head.next.next.child.next.child.next = Node(7)
c.head.next.next.child.next.child.next.next = Node(8)
ll = c.flatten()
ll
    
            
            


