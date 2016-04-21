class FastaDNA:
	def __init__(self, id = '', dna = ''):
		self.id = id
		self.dna = dna

	def __repr__(self):
		return str(self)
	def __str__(self):
		return self.id + ' ' + self.dna


def readFASTA(path):	
	data = list()

	with open(path, 'r') as input_data:
		dna = str()
		key = str()
		for line in input_data:
			if line[0] == '>':
				if(dna):
					data.append(FastaDNA(key, dna))
					dna = str()

				key = line[1:-1]
			else:
				dna += line.rstrip('\n')

		data.append(FastaDNA(key, dna))

	return data
