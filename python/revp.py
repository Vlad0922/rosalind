'''
http://rosalind.info/problems/revp/

Given: 
A DNA string of length at most 1 kbp in FASTA format.

Return: 
The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
'''

import sys

from common import readFASTA, revcomp_DNA

def main():
    data = readFASTA(sys.argv[1])

    dna = data.dna
    n = len(dna)
    revc = revcomp_DNA(dna)
    locations = list()

    for l in range(4, 13):
        for i in range(n - l + 1):
            if dna[i:i + l] == revc[i:i + l]:
                locations.append(str(i + 1) + ' ' + str(l))

    print '\n'.join(locations)

if __name__ == '__main__':
    main()