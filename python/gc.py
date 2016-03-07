'''
http://rosalind.info/problems/gc/

The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: 
At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: 
The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''

import sys

def main():
	#map with key == Rosalind_*** and 2 values: dna and percent
	data = dict()

	with open(sys.argv[1], 'r') as input_data:
		dna = str()
		key = str()
		for line in input_data:
			if line[0] == '>':
				if(dna):
					dna = dna.translate(None, '\n')
					data[key] = [dna, 0.]
					dna = str()

				key = line[1:]
			else:
				dna += line

		dna = dna.translate(None, '\n')
		data[key] = [dna, 0.]

	max = ['', 0.]

	for key in data:
		dna = data[key][0]
		count = 0
		for i in dna:
			if i == 'G' or i == 'C':
				count += 1

		prc = float(count)/len(dna)

		if(prc > max[1]):
			max[0] = key
			max[1] = prc

	print max[0], max[1]*100

if __name__ == '__main__':
    main()