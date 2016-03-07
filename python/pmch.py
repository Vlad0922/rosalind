'''
http://rosalind.info/problems/pmch/

Given: 
An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: 
The total possible number of perfect matchings of basepair edges in the bonding graph of s.
'''

import sys
from math import factorial

def main():
	with open(sys.argv[1], 'r') as data:
		lines = data.readlines()
		rna = str()
		for i in range(1, len(lines)):
			rna += lines[i]

	print rna

	n = factorial(rna.count('A'))*factorial(rna.count('C'))

	print n

if __name__ == '__main__':
    main()