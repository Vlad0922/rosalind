'''
http://rosalind.info/problems/cons/

Given: 
A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: 
A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
'''

import sys
from common import readFASTA

def getMaxProb(d):
	max = ['A', 0.]

	for key in d:
		if d[key] > max[1]:
			max[0] = key
			max[1] = d[key]

	return max[0]

def main():
	data = readFASTA(sys.argv[1])
	dna_len = len(data[0][1])
	profile = [{'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}]*dna_len

	for i in range(dna_len):
		count = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
		for j in range(0, len(data)):
			dna = data[j][1]
			count[dna[i]] += 1

		profile[i] = count

	dna = str()
	for pair in profile:
		dna += getMaxProb(pair)

	print dna

	for nuc in 'ACGT':
		line = nuc + ':'
		for pair in profile:
			line += ' ' + str(pair[nuc])
			
		print line

if __name__ == '__main__':
    main()