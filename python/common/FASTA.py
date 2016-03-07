def readFASTA(path):	
	data = list()

	with open(path, 'r') as input_data:
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

	return data
