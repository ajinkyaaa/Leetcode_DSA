
from collections import abc
from distutils import bcppcompiler
from re import A


result = []
def backTrack(wrd,result):
    if len(wrd) == 0:
        print(result)
        return result
    
    else:
        
        for i in range(len(wrd)):
            backTrack(wrd[:i] + wrd[i+1:],result+[wrd[i]])
            
backTrack("abcd",result)
print(result)

    #         abc
    #     ab      bc
    #  a      b  b    c

#   a   b   c   d