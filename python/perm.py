'''
http://rosalind.info/problems/perm/

Given: 
A positive integer n<=7.

Return: 
The total number of permutations of length n, followed by a list of all such permutations (in any order).
'''

import sys
from itertools import permutations

def main():
	with open(sys.argv[1], 'r') as data:
		n = int(data.readline().rstrip('\n'))
		sets = range(1, n + 1)

	perms = list(permutations(sets))

	print len(perms)

	for permutation in perms:
		print  ' '.join(map(str, permutation))

if __name__ == '__main__':
    main()