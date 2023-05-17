"""

                        10
                    5          20
                2     6      15     25
                        21

10 => lessthan = float("inf") 
      largerthan = float("-inf")

5 = > lessThan = 10
      largerThan = float(-inf)

20 = lessThan = float("inf)
     largerthan = 10 




"""

def validBinaryTree(root,lessThan = float("inf"),largerThan = float("-inf")):
    if root is None:
        return True

    if root.val > lessThan or root.val < largerThan:
        return False
    else:
        return validBinaryTree(root.left, min(root.val,lessThan), largerThan) and validBinaryTree(root.right,lessThan,max(largerThan,root.val))

    return True

class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.right = None
        self.left = None


    def insert(self,val):
        node = self 

        if node:
            if val < node.val:
                if node.left:
                    node.left.insert(val)
                else:
                    node.left = Node(val)
            if val > node.val:
                if node.right:  
                    node.right.insert(val)
                else:
                    node.right = Node(val)
        else:
            node = Node(val)
       

        return node

    def print(self,root):
        node = root
        arr = []
        while node:
            arr.append(node.val)
            arr += node.print(node.left)
            arr += node.print(node.right)

        print(arr)

c = Node(10)
c.insert(5)
c.insert(20)
c.insert(2)
c.insert(6)
c.insert(15)
c.insert(25)

c.left.right = Node(9)

ans = validBinaryTree(c)
print(ans)