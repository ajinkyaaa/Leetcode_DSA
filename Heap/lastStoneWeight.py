import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:
        arr = []
        for i in stones:
            heapq.heappush(arr,-i)
        lengthArr = len(arr)
        while lengthArr>1:
            val1 = -heapq.heappop(arr)
            val2 = -heapq.heappop(arr)
            diff = val1-val2
            if diff != 0:
                heapq.heappush(arr,-diff)
                lengthArr -= 1
            else:
                lengthArr -= 2
        
        if len(arr) == 0:
            return 0
        else:
            return -heapq.heappop(arr)