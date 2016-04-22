'''
http://rosalind.info/problems/prot/

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: 
The protein string encoded by s
.
'''

import sys

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

	return d


def main():
	with open(sys.argv[1], 'r') as data:
		rna = data.readline()

	t = generateTable()
	protein = str()

	for i in range (0, len(rna) - 3, 3):
		c = t[rna[i:i+3]]
		if(c == 'Stop'):
			break

		protein += c

	print protein


if __name__ == '__main__':
    main()
