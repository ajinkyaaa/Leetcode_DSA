"""
6   5   5                           5   5   6
7   6   2                           2   6   7

556 +
267 
------
l1 + l2  = 13 > 10 , 
divisor = 13 // 10 = 1
mod = 13%10 = 3

carry = divisor
mod will be added to linkedlist

3   2   8

"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LL:
    def __init__(self):
        print("")

    def addLL(self,l1,l2):
        carry = 0
        l3 = res =  Node(0)
        ans = []
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            val = n1+n2 + carry
            divisor = val // 10 #1
            mod = val % 10  #3
            
            carry = divisor #1
            l3.next = Node(mod) # 3
            ans.append(str(mod))
            l3 = l3.next


        return "".join(reversed(ans))

l1 = Node(6)
l1.next = Node(5)
l1.next.next = Node(5)

l2 = Node(7)
l2.next = Node(6)
l2.next.next = Node(2)

c = LL()
ans = c.addLL(l1,l2)
print(ans)


