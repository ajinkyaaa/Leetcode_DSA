def inOrderSuccessor(this, root,n): 
    
    successor = None
    while root:
        if n < root.data:
            successor = root
            root = root.left
        elif n >= root.data:
            root = root.right
        elif root.data == n:
            root = root.right
    return successor.val