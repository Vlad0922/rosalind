'''
http://rosalind.info/problems/mrna/

Given: 
A protein string of length at most 1000 aa.

Return: 
The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
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
			
			if d.get(words[1]) == None:
				d[words[1]] = [words[0]]
			else:
				d[words[1]].append(words[0])

	return d

def main():
	with open(sys.argv[1], 'r') as data:
		dna = data.readline().rstrip('\n')

	t = generateTable()
	total = len(t['Stop'])

	for i in dna:
		total *= len(t[i])
		print t[i]
		if total >= 1000000:
			total %= 1000000

	print total

if __name__ == '__main__':
    main()
