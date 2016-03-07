'''
http://rosalind.info/problems/hamm/

Given: Two DNA strings ss and tt of equal length (not exceeding 1 kbp).

Return: The Hamming distance
'''

from string import maketrans
import sys

def Hamming(s, t):
	count = 0

	for i in range(0, len(s)):
		if(s[i] != t[i]):
			count += 1

	return count


def main():
	with open(sys.argv[1], 'r') as data:
		s = data.readline()
		t = data.readline()

	print Hamming(s, t)

if __name__ == '__main__':
    main()
