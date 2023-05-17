class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
class LL:
    def __init__(self) -> None:
        self.head = None
    
    def add(self,val):
        if self.head:
            n = Node(val)
            n.next = self.head
            self.head = n
        else:
            self.head = Node(val)

    def print(self):
        node = self.head
        arr = []
        while node:
            print(node.val)
            arr.append(node.val)
            node = node.next
        return arr

    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        self.head = prev
        

    
c = LL()
c.add(1)
c.add(2)
c.add(3)
c.add(4)
c.add(5)
c.print()
c.reverse()
c.print()