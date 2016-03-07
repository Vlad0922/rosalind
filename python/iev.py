'''
http://rosalind.info/problems/iev

Given: 
Six positive integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa

Return: 
The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
'''

import sys

# Probabilities of Child Dominant Genotype
# ----------------------------------------
# s[0]: AA-AA -> 100% chance of dominant
# s[1]: AA-Aa -> 100%
# s[2]: AA-aa -> 100%
# s[3]: Aa-Aa -> 75%
# s[4]: Aa-aa -> 50%
# s[5]: aa-aa -> 0%

def generateProbs():
	p = [1, 1, 1, 0.75, 0.5, 0]
	return p

def main():
	with open(sys.argv[1], 'r') as data:
		s = data.readline().rstrip('\n').split()

	p = generateProbs()
	result = 0

	for i in range(0, len(s)):
		result += 2*int(s[i])*p[i]

	print result

if __name__ == '__main__':
    main()