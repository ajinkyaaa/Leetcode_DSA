# using breadth first search
while True:
    head = q.get()

    # Make sure 'head' is a power of 2 greater or equal to 2 and not visited before 'steps ' can be increased
    # Meaning it would increase 'steps ' based on the left most node values on the tree
    if (head & (head-1)) == 0 and (head != 1)\
            and (head != 0) and (head not in seen):
        steps += 1

    if head == n: # return number of steps early if we have seen our winner 
        return steps 

    left_child = head*2 # create left child for node 
    right_child = head//3 # create right child for node

    if left_child not in seen: # only traverse through this left child node later on if it has not been visited
        q.put(left_child)
    if left_child not in seen:  # only traverse through this right child node later on if it has not been visited
        q.put(right_child)

    seen.add(head)