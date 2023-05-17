def numPairsDivisibleBy60(self, time) -> int:
    arr=[0]*61
    count=0
    for i in range(len(time)):
        temp=time[i]%60
        count+=arr[-temp%60]
        arr[temp]+=1
    return count