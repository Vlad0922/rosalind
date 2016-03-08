'''
http://rosalind.info/problems/lcsm/

Given: 
A collection of kk (k<=100) DNA strings of length at most 1 kbp each in FASTA format.

Return: 
A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
'''

import sys
from common import readFASTA

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    return substr

def main():
	data = readFASTA(sys.argv[1])

	dna = list()
	for fasta in data:
		dna.append(fasta[1])


	longest = long_substr(dna)

	print longest

if __name__ == '__main__':
    main()