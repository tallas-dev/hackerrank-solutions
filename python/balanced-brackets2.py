

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
 def invBracket(ch1):
        if ch1 == '}':
            return '{'
        if ch1 == ']':
            return '['
        if ch1 == ')':
            return '('

def isBalanced(s):
    # Write your code here
    bracketstk = []
   
   # print(s)
    if len(s) < 2:
        return "NO"
    #bracketstk.append(s[0])
    for ch in s:
        if not bracketstk:
            bracketstk.append(ch)
            continue
    #    print(bracketstk)
     #   print(f'ch = {ch} invB = {invBracket(ch)}')
        if bracketstk[-1] == invBracket(ch):
      #      print('POP')
            bracketstk.pop()
        else:
       #     print('APP')
            bracketstk.append(ch)
    if bracketstk:
        return "NO"
    return "YES"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

