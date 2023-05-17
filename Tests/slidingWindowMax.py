"""
1,  3,  -1, -3, 5,  3,  6,  7
l
r
q[0(1)] popq if l > q[0]

1,  3,  -1, -3, 5,  3,  6,  7
l
    r
q[1(3)] 

1,  3,  -1, -3, 5,  3,  6,  7
l
        r
q[1(3),2(-1)] ,r+1 >=k then append that value to res and increment l

1,  3,  -1, -3, 5,  3,  6,  7
    l
            r
q[1(3),2(-1),3(-3)]  r+1 >= k then append q[0] tp res and increment l

1,  3,  -1, -3, 5,  3,  6,  7 l > q[0] then pop 
        l
                r
q[4(5)]
"""

from collections import deque
def slidingWindowMax(arr,k):
    l = 0
    r = 0
    res = []
    q = deque()
    while r<= len(arr)-1:
        while q and arr[r]>q[-1]:
            q.pop()
        q.append(r) #q = [index 1 (val 3)]

        if l > q[0]:
            q.popleft()
        if r-l+1 >= k:
            res.append(arr[q[0]])
            l += 1
        r += 1
    
    return res

ans = slidingWindowMax([1,  3,  -1, -3, 5,  3,  6,  7],3)
print(ans)
