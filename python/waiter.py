
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#
def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def waiter(number, q):
    primes = generate_primes(q)
    answers = []

    for i in range(q):
        A = []  # Plates not divisible by the prime
        B = []  # Plates divisible by the prime

        while number:
            plate = number.pop()
            if plate % primes[i] == 0:
                B.append(plate)
            else:
                A.append(plate)

        answers.extend(B[::-1])  # Collect B in reverse order
        number = A  # Update for the next iteration

    answers.extend(number[::-1])  # Collect any remaining plates in reverse order
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

