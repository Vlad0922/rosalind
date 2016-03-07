'''
http://rosalind.info/problems/grph/

Given: 
A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: 
The adjacency list corresponding to O(3) You may return edges in any order.
'''

import sys

problem = 'grph'

out_folder = 'output'
output_file = out_folder + '/' + problem + '.txt'

def main():
	data = list()

	with open(sys.argv[1], 'r') as input_data:
		dna = str()
		key = str()
		for line in input_data:
			if line[0] == '>':
				if(dna):
					data.append((key, dna))
					dna = str()

				key = line[1:-1]
			else:
				dna += line.rstrip('\n')

		data.append((key, dna))

	k = 3

	pairs = list()

	for i in range(0, len(data)):
		for j in range(0, len(data)):
			if data[i][1][-k:] == data[j][1][:k] and i != j:
				pairs.append((data[i][0], data[j][0]))

	print 'done!'

	with open(output_file, 'w') as out:
		for i in pairs:
			out.write(i[0] + ' ' + i[1] + '\n')


if __name__ == '__main__':
    main()