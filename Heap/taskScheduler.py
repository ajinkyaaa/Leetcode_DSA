
import heapq
from collections import deque,defaultdict

#[-3,-3]
class Solution:
    def leastInterval(self, tasks, n: int) -> int:

        heapArr = []
        queue = deque()
        time = 0

        dic = defaultdict(int)
        for i in tasks:
            dic[i] += 1
        
        
        taskCounts = list(dic.values())

        for i in taskCounts:
            heapq.heappush(heapArr,-i)
        
        while heapArr or queue:
            time += 1 # 1
            if heapArr:
                val = -heapq.heappop(heapArr)  #[3] 
                val = val -1 #[2]
            
                
                if val != 0:
                    queue.append([val,time+ n]) # [[2,3]]
            
                
            while queue and queue[0][1] <= time:

                nextTask = queue.popleft()
                heapq.heappush(heapArr,-nextTask[0])
        return time    
