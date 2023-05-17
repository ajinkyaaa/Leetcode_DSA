
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.child = None

n1 = Node(1)
n2= Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)
n11 = Node(11)
n12 = Node(12)


n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n7.next = n8
n8.next = n9
n9.next = n10
n11.next = n12


n3.child = n7
n8.child = n11





root = n1

class Solution:
    def flatten(self, head):
        stack = []
        if not head:
            return head
        dummy = Node(0)
        node = dummy

        stack.append(head)
        while stack:
            n = stack.pop()
            nextNode = n.next
            child = n.child
            if nextNode is not None:
                stack.append(nextNode)
                #print("next",stack[-1].val)
            if child is not None:
                stack.append(child)
                #print("child",stack[-1].val)
            node.next = n
            n.prev = node
            node.child = None
            node = n
        dummy.next.prev = None
        return dummy.next

s = Solution()
ans = s.flatten(root)

"""
while ans:
    print(ans.val)
    ans = ans.next
"""