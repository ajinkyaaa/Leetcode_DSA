"""
7,0,1,2,3,4,5,6
0,1,2,3,4,5,6,7
5,6,7,0,1,2,3,4

5,6,7,0,1,2,3,4, target = 5
mid = 1

if target = mid then return
if target > 1 and target <5, l= mid+1, else r = mid -1

if target = 0
if target < 1 and target > 4, r = mid-1,else l = mid +1
"""

def searchRotatedArray(arr,target):
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = (r+l)//2
        if target == arr[mid]:
            return mid
        

        if arr[mid] > arr[l]:
            if target < arr[l] or target > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target > arr[r] or target < arr[mid]:
                r = mid -1
            else:
                l = mid + 1
    return -1

print(searchRotatedArray([5,6,7,0,1,2,3,4],1))
