from DNA_RNA import DNA_to_RNA

__p_table = dict()

def __read_table():
	with open('data/prot_table.txt', 'r') as table:
		for l in table:
			words = l.rstrip('\n').split(' ')
			__p_table[words[0]] = words[1]

def DNA_to_PROT(dna):
	rna = DNA_to_RNA(dna)

	if(len(__p_table) == 0):
		__read_table()

	protein = str()
	for i in range (0, len(rna) - 3, 3):
		c = __p_table[rna[i:i+3]]
		if(c == 'Stop'):
			break

		protein += c

	return protein

