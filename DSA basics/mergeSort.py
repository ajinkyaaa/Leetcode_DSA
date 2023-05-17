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
  
# # Input list 
# a = [12, 11, 13, 5, 6, 7] 
# print("Given array is") 
# print(*a) 
  
# a = merge_sort(a) 
  
# # Print output 
# print("Sorted array is : ") 
# print(*a) 

def merge_sort2(values): 
  
    if len(values)>1: 
        m = len(values)//2
        left = values[:m] 
        right = values[m:] 
        right = merge_sort2(right) 
        left = merge_sort2(left) 
        
  
        values =[] 
  
        while len(left)>0 and len(right)>0: 
            val = left.pop()
            values.append(val)
            val = right.pop()
            values.append(val)

  
        for i in left: 
            values.append(i) 
        for i in right: 
            values.append(i) 
                  
    return values 

print(merge_sort2(["a1","b1","c1","a2","b2","c2"]))