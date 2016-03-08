'''
http://rosalind.info/problems/lexv/

Given: 
A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n<=4).

Return: 
All strings of length at most n formed from A, ordered lexicographically.
'''

import sys
from itertools import product
from math import pow

def main():
    with open(sys.argv[1], 'r') as data:
        alphabet = data.readline().rstrip('\n').split()
        n = int(data.readline())

    perms = list()
    for i in range(1, n + 1):
    	perms.extend([''.join(p) for p in product(alphabet, repeat = i)])

    char_table = dict()
    for i in range(len(alphabet)):
    	char_table[alphabet[i]] = i

    alpha_len = len(alphabet)

    def lex_sort(s):
    	h = 0
    	for i in range(len(s)):
    		h += pow(alpha_len, n - 1 - i)*char_table[s[i]]
    		
    	return h

    perms = sorted(perms, key = lambda x : (lex_sort(x), x))

    with open('output/lexv.txt', 'w') as output:
    	output.writelines('\n'.join(perms))

if __name__ == '__main__':
    main()