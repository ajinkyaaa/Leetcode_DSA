#!/bin/python3

import math
import os
import random
import re
import sys


def multiply(a, b, bound):
    # write your code here
    
    res = a*b
    if res <= bound:
        return res
    else:
        raise ValueError("multiplication of "+str(a)+" and "+str(b)+ " with bound " +str(res)+ " not possible")
    
m  = multiply(5,2,9)
