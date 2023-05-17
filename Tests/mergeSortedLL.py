"""
1   2   6   
4   5   8   10

use case:-
add any one if same
return type => int array
all values int

l1 or l2

"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LL:
    def __init__(self):
        self.head= None

    def mergeLL(self,l1,l2):
        ans = []
        l3 = res =  Node(0)
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = Node(l1.val)
                ans.append(l1.val)
                l1 = l1.next
                l3 = l3.next
            else:
                l3.next = Node(l2.val)
                ans.append(l2.val)
                l2 = l2.next
                l3 = l3.next

        
        while l1:
            l3.next = Node(l1.val)
            ans.append(l1.val)
            l1 = l1.next
            l3 = l3.next
        while l2:
            l3.next = Node(l2.val)
            ans.append(l2.val)
            l2 = l2.next
            l3 = l3.next

        print(ans)
        return res.next

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(6)

l2 = Node(4)
l2.next = Node(5)
l2.next.next = Node(8)
l2.next.next.next = Node(10)

c = LL()
res = c.mergeLL(l1,l2)
print(res)






