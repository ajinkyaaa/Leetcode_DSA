class Node:
    def __init__(this,val):
        this.val = val
        this.next = None
        this.child = None
        this.prev = None

class singlyLinkedList:
    def __init__(this):
        this.head = None
        
    def addNode(this,val):
        if this.head is None:
            this.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = this.head
            this.head = new_node
            
    def printNode(this,node):
        
        if node:
            print(node.val)
            node = node.next
            this.printNode(node)

    def reverse(this):
        cur = this.head
        prev = None
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        this.head = prev
        return prev

            
s = singlyLinkedList()
s.addNode(1)
s.addNode(2)
s.addNode(3)

s.printNode(s.head)
s.reverse()
s.printNode(s.head)
