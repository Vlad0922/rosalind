'''
http://rosalind.info/problems/rna/

Problem

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string tt corresponding to a coding strand, its transcribed RNA string uu is formed by replacing all occurrences of 'T' in tt with 'U' in uu.

Given: 
A DNA string tt having length at most 1000 nt.

Return: 
The transcribed RNA string of tt.
'''

import sys

def main():
	with open(sys.argv[1], 'r') as data:
		dna = data.read().strip();

	dna = dna.replace('T', 'U')
	dna = dna[::-1]

	print dna

if __name__ == '__main__':
    main()
