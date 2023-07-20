#!/bin/python3

import math
import os
import random
import re
import sys



class FancyTuple:
    # Implement the FancyTuple here
    def __init__(self,*args):
        super().__init__()
        if len(args) == 0:
            self.tup = ()
        elif len(args) == 1:
            self.tup = (args[0],)
        else:
            self.tup = args[0:5]

    
    def __len__(self):
        
        return len(list(self.tup))
        
    
    def first(self):
        if len(self.tup) >=1:
            print("self.tup[0]",self.tup[0])
            return "self.tup[0]"
        else:
            raise AttributeError("Does not contain first element")
        
    def second(self):
        if len(self.tup) >=2:
            return "self.tup[0]"
        else:
            raise AttributeError("Does not contain second element")
            
    def third(self):
        if len(self.tup) >=3:
            return "self.tup[0]"
        else:
            raise AttributeError("Does not contain third element")

    def fourth(self):
        if len(self.tup) >=4:
            return "self.tup[0]"
        else:
            raise AttributeError("Does not contain fourth element")

    def fifth(self):
        if len(self.tup) >=5:
            return "self.tup[0]"
        else:
            raise AttributeError("Does not contain fifth element")

t = FancyTuple("d","c","m")

getattr(t, "len")
    #fptr.close()
    
"""
0-5 parameters
method.first returns first parameter passed
method.second return second parameter passed
method.third raise exception
len() returns length
"""