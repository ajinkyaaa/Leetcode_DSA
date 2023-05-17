def solution(A):
    # Implement your solution here
    A.sort()
    print(A)
    dic = {}
    maxSum = float("-inf")
    counter = 0
    for i,num in enumerate(A):
        counter = i+1
        while counter < len(A):

            for char in str(A[counter]):

                print(A[counter])
            
from collections import defaultdict
def solution2(A):
    # Implement your solution here
    
    print(A)
    dicFirstLastIndexNumber = defaultdict(list)
    maxSum = -1
    counter = 0
    for i,num in enumerate(A):
        lenNum = len(str(num))
        if (str(num)[0],str(num)[lenNum-1]) in dicFirstLastIndexNumber:
            maxSum = max(dicFirstLastIndexNumber[str(num)[0],str(num)[lenNum-1]]+num,maxSum)
            dicFirstLastIndexNumber[(str(num)[0],str(num)[lenNum-1])] = max(dicFirstLastIndexNumber[(str(num)[0],str(num)[lenNum-1])],num)

        else:
            dicFirstLastIndexNumber[(str(num)[0],str(num)[lenNum-1])] = num
    
    print(dicFirstLastIndexNumber)
    print(maxSum)
#solution2([130,191,200,10])
"""
dicFirstLastIndexNumber = defaultdict(list)
dicFirstLastIndexNumber[(2,3)] = [1]
if (2,4) in dicFirstLastIndexNumber:
    print("true")
"""

def solution3(numbers):
    maximumEven = float("-inf")
    maximumOdd = float("-inf")
    if len(numbers) == 0:
        return 0
    for x in numbers:
        if x % 2 == 0 and x > maximumEven:
            maximumEven = x
        elif x % 2 != 0 and x > maximumOdd:
            maximumOdd = x
    maximumEven = maximumEven if maximumEven !=  float("-inf") else 0
    maximumOdd = maximumOdd if maximumOdd !=  float("-inf") else 0
    print(maximumEven + maximumOdd)

solution3([-1])