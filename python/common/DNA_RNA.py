from string import maketrans

def DNA_to_RNA(dna):
    return dna.replace('T', 'U')

def RNA_to_DNA(rna):
    return rna.replace('U', 'T')

def comp_DNA(dna):
	trans = maketrans('ATCG', 'TAGC')
	return dna.translate(trans)

def revcomp_DNA(dna):
    res = comp_DNA(dna)
    return res[::-1]

