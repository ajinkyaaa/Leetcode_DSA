"""
words = ["wrt","wrf","er","ett","rftt"]

w =>r =>t
w =>r =>f
e =>r
e =>t =>t
r =>f =>t =>t
                                w                       e                                   r
                                r                   r       t                           f
                            t       f                           t                   t
                                                                                t
order:
w:0
r:1
t:2
f:2

e:0
r:1
t:1

r:0
f:1
t:2

order
{
    w:0,
    e:0
    r:2
    t:5
    f:3
}

dic = {
    w:[r,t,f],
    r:[t,f],
    t:[],
    e:[r,t],
    f:[t]
}

add order 0 values to queue
pop value and add to result, check for neighboring nodes, decrement their order, if order = 0 then we add to queue

if order = 0, add to ans
use bfs with queue, k = k-1, if k = 0, add to res else add back to queue

"""
arr = ["wrt","wrf","er","ett","rftt"]
from collections import defaultdict,deque
class AlienDic:
    def __init__(self,arr):
        self.arr = arr
        self.dic = defaultdict(list)
        self.order = defaultdict(int)
        self.res = []

    def getRes(self):
        q = deque()
        for i,wrd in enumerate(self.arr):
            visited = []
            for j,c in enumerate(wrd):
                self.order[c] = 0

        for i,wrd in enumerate(self.arr):
            visited = []
            for j,independant in enumerate(wrd):
                for dependant in wrd[j+1:]:
                    if dependant not in self.dic[independant] and dependant != independant:
                        self.dic[independant].append(dependant)
                        self.order[dependant] += 1



        
        for c in self.order.keys():
            if self.order[c] == 0:
                q.append(c)
                
        
        print(self.dic)
        print(self.order)
        print(q)

        while q:
            val = q.popleft()
            self.res.append(val) #w

            for c in self.dic[val]:#['r', 't', 'f']
                self.order[c] -= 1
                if self.order[c] == 0:
                    q.append(c)

        print(self.res)

c = AlienDic(arr)
c.getRes()


