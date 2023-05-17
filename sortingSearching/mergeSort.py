class Solution:
    def mergeSort(self,arr):

        if len(arr)>1:
            l = 0
            r = len(arr)
            m = l+(r-l)//2

            left = self.mergeSort(arr[:m])
            right = self.mergeSort(arr[m:])

            arr = []
            while left and right:
                if left[0] < right[0]:
                    arr.append(left.pop(0))
                else:
                    arr.append(right.pop(0))
            while left:
                arr.append(left.pop(0))
            while right:
                arr.append(right.pop(0))
        return arr

c = Solution()
print(c.mergeSort([5,4,3,2,1]))

def merge_sort(values): 
  
    if len(values)>1: 
        m = len(values)//2
        left = values[:m] 
        right = values[m:] 
        left = merge_sort(left) 
        right = merge_sort(right) 
  
        values =[] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                values.append(left[0]) 
                left.pop(0) 
            else: 
                values.append(right[0]) 
                right.pop(0) 
  
        for i in left: 
            values.append(i) 
        for i in right: 
            values.append(i) 
                  
    return values 

print(5%4)