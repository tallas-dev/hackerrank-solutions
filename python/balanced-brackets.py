
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
def isBalanced(s):
    stack = []
    pairs = {"{": "}", "[": "]", "(": ")"}

    for char in s:
        if char in pairs:  # opening brackets
            stack.append(char)
        elif stack and char == pairs[stack[-1]]:  # closing brackets with matching pair
            stack.pop()
        else:
            return "NO"  # unmatched closing bracket

    return "YES" if not stack else "NO"    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

