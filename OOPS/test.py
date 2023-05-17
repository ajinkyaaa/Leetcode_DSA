list = [1,2]
list[0] = 5
print(list)

tupleA = (1,2)
print(tuple)
a = "abc"
b = a
b = "bcd"
print(a)
print(b)

print("aba"[::-1] == "aba")
tupleB = tupleA
tupleB +=("a","b")
print(tupleA)
print(tupleB)


def printStar(num):
    for i in range(5):
        print("* ",end ="") 
        print()

printStar(4)