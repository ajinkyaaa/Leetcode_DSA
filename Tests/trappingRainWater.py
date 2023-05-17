"""
height = [0,1,0,2,1,0,1,3,2,1,2,1]

                            ___
             __            |   | __     ___
     __     |   |__      __|   |   |___|   |__
    |  |    |   |  |   |   |   |   |   |   |  |
    1     1   2   2  2   2   3   3   3   3   3
    3     3   3   3  3   3   3   2   2   2   1



"""

def trapRainWater(height):
    arr = [0] * len(height)
    leftMax = 0
    for i,h in enumerate(height):
        leftMax = max(leftMax,h)
        arr[i] = leftMax
    
    

    rightMax = 0
    for i,h in reversed(list(enumerate(height))):
        rightMax = max(rightMax,h)
        arr[i] = min(arr[i],rightMax) - h
    
    return sum(arr)

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapRainWater(height))
