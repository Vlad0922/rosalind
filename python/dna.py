'''
http://rosalind.info/problems/dna/

Problem

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: 
A DNA string ss of length at most 1000 nt.

Return: 
Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.
'''
import sys

def main():
	with open(sys.argv[1], 'r') as data:
		dna = data.read().strip();

	count = {'A':0, 'C':0, 'G':0, 'T':0}

	for i in range (0, len(dna)):
		count[dna[i]] += 1

	print count['A'], count['C'], count['G'], count['T']

if __name__ == '__main__':
    main()
