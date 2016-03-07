'''
http://rosalind.info/problems/orf/

Given: 
A DNA string s of length at most 1 kbp in FASTA format.

Return: 
Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
'''

import sys
from string import maketrans

'''
RNA codon table
***************
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G 
'''

def generateTable():
	d = dict()
	with open('data/prot_table.txt', 'r') as table:
		for l in table:
			words = l.rstrip('\n').split(' ')
			d[words[0]] = words[1]

	d['ATG'] = 'M'

	return d


def main():
	with open(sys.argv[1], 'r') as data:
		dna = data.readlines()[1].rstrip('\n')

	dna = dna.replace('T', 'U')
	t = generateTable()
	protein = str()
	starting = False
	trans = maketrans('ATCG', 'TAGC')

	dna_list = [dna]
	dna_list.append(dna.translate(trans))

	print dna_list

	for i in range(0, len(dna) - 2):
		if t[dna[i:i+3]] == 'M': #start codon
			for j in range(i, len(dna) - 2, 3):
				c = t[dna[j:j + 3]]

				if c == 'Stop':
					print protein
					protein = str()
					i = j
					break
				else:
					protein += c

	print protein


if __name__ == '__main__':
    main()