'''
http://rosalind.info/problems/sign/

Given: 
A positive integer n<=6

Return: 
The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).
'''

import sys

import math
import itertools

def elem_multiply(x, y):
    return [a*b for a, b in zip(x, y)]

def main():
    with open(sys.argv[1]) as input:
        n = int(input.readline())

    count = int(math.factorial(n)*math.pow(2, n))
    result = list()

    base = list(itertools.permutations(xrange(1, n + 1)))
    mask = list(itertools.product([1, -1], repeat = n))

    print count
    for b in base:
        for m in mask:
            print ' '.join(map(str, elem_multiply(b, m)))


if __name__ == '__main__':
    main()