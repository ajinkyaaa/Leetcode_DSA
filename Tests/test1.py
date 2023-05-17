"""
Blocks = [
    {
        "gym" :False,
        "school": True
        "store":False
    },
        {
        "gym" :True,
        "school": False
        "store":False
    },
        {
        "gym" :True,
        "school": True
        "store":False
    },
        {
        "gym" :False,
        "school": True
        "store":True
    }

]

0 => 6
1 => 3
2 => 1
3 => 1

{
        "gym" :False,      
        "school": True, => 0
        "store":False
    }
    [None,0,None] => [1,0,None] =>[1,0,None] =>
    gym == False: => dont update
    school == True => set value min(i,currentval)
    store == False => dont update


[a,b,c,d]



"""
Blocks = [    {
        "gym" :False,
        "school": True,
        "store":False
    },
        {
        "gym" :True,
        "school": False,
        "store":False
    },
        {
        "gym" :True,
        "school": True,
        "store":False
    },
        {
        "gym" :False,
        "school": True,
        "store":True
    }]

def findApt(arr):
    totalDistance = [float("inf")] * len(arr)

    l = 0
    result = []
    for i in range(len(arr)):
        count = {
                "gym" : float("inf"),
                "school" : float("inf"),
                "store" : float("inf")

            }
        for l,val in reversed(list(enumerate(arr[:i+1]))):

            if val["gym"] == True:
                count["gym"] = min(count["gym"],l)
            if val["school"] == True:
                count["school"] = min(count["school"],l)
            if val["store"] == True:
                count["store"] = min(count["store"],l)

        for l,val in enumerate(arr[i:]):

            if val["gym"] == True:
                count["gym"] = min(count["gym"],l)
            if val["school"] == True:
                count["school"] = min(count["school"],l)
            if val["store"] == True:
                count["store"] = min(count["store"],l)

        total = 0
        result.append(sum([count["gym"],count["school"],count["store"]]))
    
    print(result)
    
    minVal = float("inf")
    ansIndex = None
    for i in range(len(result)):
        currentMax = result[i]
        if currentMax < minVal:
            minVal = currentMax
            ansIndex = i
    print(Blocks[ansIndex])
    return Blocks[ansIndex]




findApt(Blocks)

