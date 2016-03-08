'''
http://rosalind.info/problems/lexf/

Given: 
A collection of at most 10 symbols defining an ordered alphabet, and a positive integer nn (n<=10).

Return: 
All strings of length nn that can be formed from the alphabet, ordered lexicographically.
'''

import sys
from itertools import product

def main():
    with open(sys.argv[1], 'r') as data:
        alphabet = data.readline().rstrip('\n').split()
        n = int(data.readline())

        perms = [''.join(item) for item in product(alphabet, repeat = n)]

        for p in perms:
            print p

if __name__ == '__main__':
    main()