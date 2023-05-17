"""
1   2   3   4   5
1   4   3   2   5

L = 2
R = 4

prev = 1
n = cur = 2

prev = None
cur = l3 = 2
4 =>3 =>2 => None

cur.next = nextNode
next


"""
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class reverseLL:
    def __init__(self):
        self.head = None
    
    def flatten(self,left,right):
        cur = self.head
        counter = 1
        while cur:
            if counter < left or counter > right:
                cur = cur.next
                counter += 1
                continue
            if counter == left:
                n = self.reverse(cur,left,right)
                counter = right+1
                cur.next = n
            
        return self.head
                

    def reverse(self,node:Node,left,right):
        prev = None
        cur = node
        while cur and left<=right:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
            left += 1
        node.next = nextNode
        return prev

c = reverseLL()

c.head = Node(1)
c.head .next = Node(2)
c.head .next.next = Node(3)
c.head .next.next.next = Node(4)
c.head .next.next.next.next = Node(5)

c.flatten(2,4)


