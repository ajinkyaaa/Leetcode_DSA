
from collections import defaultdict
arr = [1,2,3,4]
def twoSum(arr,target):
    dic = defaultdict(int)

    for i in range(len(arr)):
        if target - arr[i] in dic:
            return [dic[target - arr[i]] ,i]
        
        dic[arr[i]] = i

print(twoSum(arr,5))

