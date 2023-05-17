def minSteps(n):

    q = deque([(1,0)])
    result = []
    while q:

        val, steps = q.popleft()

        if val == n:
            return steps
        
        q.append((val//3,steps+1))
        q.append((val * 2,steps+1))

print(minSteps(3))