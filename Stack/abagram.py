 # find_anagrams(['abba', 'fed', 'abdc', 'abc', 'defg', 'def', 'bac', 'ijkl', 'cba', 'xyzaa']) -> [(fed, def), (abc, bac, cba)]

from collections import defaultdict
def createAnagrams(arr):
    dic = defaultdict(list)

    for i in arr:
        #print(tuple(sorted(i)))
        dic[tuple(sorted(i))].append(i)
    ans = []
    for i in dic.values():
        if len(i)>1:
            ans.append(i)


 
    return ans




print(createAnagrams(['abba', 'fed', 'abdc', 'abc', 'defg', 'def', 'bac', 'ijkl', 'cba', 'xyzaa']))