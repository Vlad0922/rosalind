'''
http://rosalind.info/problems/iprb/

Given: 
Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: 
The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
'''

import sys
from math import factorial

def Permutation(n, k):
	return factorial(n)/(factorial(k)*factorial(n - k))

def main():
	with open(sys.argv[1], 'r') as data:
		k, m, n = map(float, data.readline().rstrip('\n').split(' '))

	dom = 4*Permutation(k + m + n, 2)
	total = 4*Permutation(n, 2) + 2*n*m + Permutation(m, 2)

	print 1 - total/dom

if __name__ == '__main__':
    main()