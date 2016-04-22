'''
http://rosalind.info/problems/splc/

Given: 
A DNA string s (of length at most 1 kbp) and a collection of substrings of ss acting as introns. All strings are given in FASTA format.

Return: 
A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
'''

import sys

from common import readFASTA, revcomp_DNA, DNA_to_PROT

def main():
    data = readFASTA(sys.argv[1])

    dna = data[0].dna

    for i in range(1, len(data)):
        dna = dna.replace(data[i].dna, '')

    prot = DNA_to_PROT(dna)
    print prot

if __name__ == '__main__':
    main()