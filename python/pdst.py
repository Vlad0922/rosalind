'''
http://rosalind.info/problems/pdst/

Given: 
A collection of n (n<=10) DNA strings s1...sn of equal length (at most 1 kbp). Strings are given in FASTA format.

Return: 
The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is allowed an absolute error of 0.001.
'''

import sys
from common import readFASTA
from numpy import zeros

def p_distance(s, q):
	diff = 0.

	for i in range(len(s)):
		if s[i] != q[i]:
			diff += 1

	return diff/len(s)

def main():
	data = readFASTA(sys.argv[1])

	matrix = zeros((len(data), len(data)))

	for i in range(len(data)):
		for j in range(i + 1, len(data)):
			matrix[i][j] = p_distance(data[i][1], data[j][1])
			matrix[j][i] = matrix[i][j]	# this matrix is mirrored by main diag, so we can compute only part of matrix


	for i in range(len(data)):
		line = ' '.join(map(str, matrix[i]))
		print line

if __name__ == '__main__':
    main()