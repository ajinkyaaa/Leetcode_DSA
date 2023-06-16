

"""
0   1   1   2   3   5   8   13

"""

def fibonacci(res,num):
    if num == len(res):
        return res
    else:
        return fibonacci(res + [res[-1] + res[-2]],num) 

print(fibonacci([0,1] , 10))