'''
http://rosalind.info/problems/lia/

Given:
Two positive integers kk (k<=7) and NN (N<=2*k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return:
The probability that at least NN Aa Bb organisms will belong to the kk-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors./
'''
import sys
from math import factorial

def Permutation(n, k):
	return factorial(n)/(factorial(k)*factorial(n - k))

def main():
	with open(sys.argv[1], 'r') as data:
		k, N = map(int, data.read().split())

	prob = 0.
	for i in range(N, 2**k + 1):
	    prob += Permutation(2**k, i) * ((1./4)**i) * ((3./4)**((2**k)-i))

	print prob

if __name__ == '__main__':
    main()
