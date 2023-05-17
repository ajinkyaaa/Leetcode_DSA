
from collections import defaultdict
def findTopK(arr,k):
    bucket = [[] for i in range(len(arr))]
    dicCount = defaultdict(int)

    for i in range(len(arr)):
        dicCount[arr[i]] += 1

    for n,c in dicCount.items():
        bucket[c].append(n)
    print(bucket)
   
    res = []
    for i in range(len(bucket) - 1, 0, -1):
        for n in bucket[i]:
            res.append(n)
            if len(res) == k:
                return res

print(findTopK([1,1,1,2,2,3],2))

from collections import defaultdict,heapq
class Solution:
    def topKFrequent(self, nums, k: int):
        hash_map = defaultdict(int)
        for n in nums:
            hash_map[n]+=1
        
        heap = []
        for key, val in hash_map.items():
            heapq.heappush(heap, (-val, key))
        
        res = []
        for i in range(k):
            _, key = heapq.heappop(heap)
            res.append(key)
        return res

"""
Steps:-
insert value and count in hashmap
push negative values to heap
pop k values

"""