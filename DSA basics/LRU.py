
from platform import node


class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class singlyLinkedList:
    def __init__(self,capacity) -> None:
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = 5
        self.dic = {}
        
    def _add(self,Node):
        p = self.tail.prev
        p.next = Node
        Node.next = self.tail
        Node.prev = p
        self.tail.prev = Node
    
    def _remove(self,Node):
        p = Node.prev
        n = Node.next
        p.Next = n
        n.prev = p  
              
    def addNode(self,key,val):
        if key in self.dic:
            self._remove(self.dic[key])
        newNode = Node(key,val)
        self._add(newNode)
        self.dic[key] = newNode
        if len(self.dic) > self.capacity:
            self._remove(self.dic[key])
        
"""
Steps:-
create node with key value prev and next
create ssl with head tail capacity and dic and assign thosem to each other

add:-
    check if the key is in dic, if yes then remove
    to add the node, add before tail

add to dictionary and check if greater than capacity then delete.



"""


"""
LRU
define node class
init => head <=> tail, set capacity, set size, create dictionary to store node as key
add => as doubky linked list
remove => to delete a node in dll
if size > capacity: delete  last node near tail

"""

class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRU:
    def __init__(self,capacity):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.dic = {}
        self.size = len(self.dic.keys())

    def remove(self,key):
        node = self.dic[key]
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = node


    def add(self,key,val):
        if key in self.dic:
            self.remove(key)
            del self.dic[key]
        
        node = Node(key,val)
        self.dic[key] = node
        
        node.next = self.head
        self.head = node
        if len(self.dic.keys()) > self.capacity:
            self.remove(self.tail.prev.val)

    def print(self):
        cur = self.head
        while cur.next:
            print(cur.val)
            cur = cur.next
            

lru = LRU(4)
lru.add(1,"a")
lru.add(2,"b")
lru.add(3,"c")
lru.add(4,"d")
lru.add(5,"e")
lru.add(6,"f")

lru.print()

            

