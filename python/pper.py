'''
http://rosalind.info/problems/pper/

Given: 
Positive integers nn and kk such that 0 < n <= 100 and  0 < 10 <= k

Return: 
The total number of partial permutations P(n,k), modulo 1,000,000.
'''

import sys

def Permutation(n, k):
	return factorial(n)/(factorial(k)*factorial(n - k))

def main():
	with open(sys.argv[1], 'r') as data:
		n, k = map(int, data.readline().rstrip('\n').split(' '))

	perm = 1
	for i in range(n - k + 1,n + 1):
		perm = (perm * i) % 1000000

	print perm

if __name__ == '__main__':
    main()