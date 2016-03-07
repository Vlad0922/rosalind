'''
http://rosalind.info/problems/revc/

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string ss is the string scsc formed by reversing the symbols of ss, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: 
A DNA string ss of length at most 1000 bp.

Return: 
The reverse complement scsc of ss.
'''

from string import maketrans
import sys

def main():
	with open(sys.argv[1], 'r') as data:
		dna = data.read().strip();

	trans = maketrans('ATCG', 'TAGC')

	dna = dna[::-1]
	dna = dna.translate(trans) 

	print dna

if __name__ == '__main__':
    main()
