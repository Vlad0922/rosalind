'''
http://rosalind.info/problems/prob/

Given: 
A DNA string ss of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

Return: A
An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.
'''

import sys
from math import log10
from collections import Counter

def main():
	with open(sys.argv[1], 'r') as data:
		dna, probs = data.readlines()

	probs = map(float, probs.split())
	c = Counter(dna)

	count = dict()
	count['CG'] = float(c['C'] + c['G'])
	count['AT'] = float(c['A'] + c['T'])

	gc_prob = map(str, [count['CG']*log10(0.5 * pr) + count['AT']*log10(0.5*(1. - pr)) for pr in probs])

	print ' '.join(gc_prob)

if __name__ == '__main__':
    main()