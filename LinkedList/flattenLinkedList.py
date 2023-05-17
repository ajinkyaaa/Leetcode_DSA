class Solution:
    def Node(self,val):
        self.val = val

    def flatten(self, head):
        stack = []
        if not head:
            return head
        dummy = self.Node(0)
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