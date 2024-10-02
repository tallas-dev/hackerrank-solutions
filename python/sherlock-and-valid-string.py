# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    checkset = {}
    if len(s) == 1:
        return 'YES'
        
    for ch in s:
        if ch in checkset:
            checkset[ch] += 1
        else:
            checkset[ch] = 1
    occs = sorted(checkset.values())
    # occs_set = set(occs)
    # if len(occs_set) > 2:
    #     return 'NO'
    # if len(occs_set) == 1:
    #     return 'YES'
    if occs[0] != 1 and occs[0] == occs[-1] - 1:
        return 'YES'
    if occs[0] == 1 and occs[1] == occs[-1]:
        return 'YES'
    if occs[0] == occs[-1]:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')
    
    fptr.close()


