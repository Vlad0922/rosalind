'''
http://rosalind.info/problems/splc/

Given: 
A DNA string s (of length at most 1 kbp) and a collection of substrings of ss acting as introns. All strings are given in FASTA format.

Return: 
A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
'''

import sys

from common import readFASTA, revcomp_DNA

def main():
    data = readFASTA(sys.argv[1])

    print data

if __name__ == '__main__':
    main()