"""
Problem statement:-
Inputs are 
A= 20
B= 20
C=20
D=40
Out Put :
If we remove D
should be like the below after distributing share of D equally between amongst A,B,C
A= 33.33
B= 33.33
C= 33.33

op:-

A ,B C ,D 

del D=40 => remaining elements => 3
            dic.keys -1 =3 
        val D/3 = 13.33 
        del key
        add value to all other keys



"""
from collections import defaultdict

dic = defaultdict(int)
dic["A"] =20
dic["B"] =20
dic["C"] =20
dic["D"] =40

print(dic.keys())
def delKey(dic,key):

    #lDic = dic.keys() -1
    if key not in dic:
        return False
    
    if key in dic:
        val = dic[key]/(len(dic.keys())-1)
        del dic[key]

        for k in dic.keys():
            dic[k] += val
            print(dic[k])

#delKey(dic,"D")

"""
Top n frequent word formed by unique character
Seq(
John, Robert, Mathew 
Ajay, Vijay,  Singh
Sachin Raj  Robert
Sachin Raghav  Rajat
Sachin Vijay  Singh
Ravi Raj Bhawani
)

requirement:-
john = 0 repeating chars  take john
Robert = r repeating => skip

define user define f to filter records

john,Mathew,john,vijay



df
Sachin 3
john 2
mathew 1
vijay 1

udf = checkRepeatingChar(wrd):
         if wrd = set(wrd):
            return wrd
         else:
            return None

df = df.filter(checkRepeatingChar("name")).dropna()

groupBy = df.select("name","count").groupBy("name").agg(count("name").orderBy("desc").alias("count"))

select name,count from df group by name order by count desc

df
======
name
Sahin
john
mathew

sum=18 combining 3 number from the below array
1,2,3,4,5,7,6,9,8 target=18


1,  2,  3,  4,  5,  6,  7,  8,  9 
    i
        l                       r 

    if i+l+r > target:
    if i+l+r < target
    if i+l+r = targt => save it to result arr


input
       1
     2  3

expected     
     1
  3        2
4  5

node =1
node.left = 3
node.right =2

node.left,node.right = node.right,node.left


def swapNodes(root):
    if root is None:
        return
    if root:
        root.left ,root.right = root.right,root.left
        swapNodes(root.left)
        swapNodes(root.right)
    return root

"""

