'''
http://rosalind.info/problems/kmp/

Given: 
A DNA string s (of length at most 100 kbp) in FASTA format.

Return: 
The failure array of s.
'''

'''
http://e-maxx.ru/algo/prefix_function
'''

import sys

from common import readFASTA

def main():
    data = readFASTA(sys.argv[1])
    dna = data.dna

    fail = [0]*len(dna)
    fail[0] = 0

    for i in range(1, len(dna)):
        j = fail[i-1]

        while(j > 0 and dna[i] != dna[j]):
            j = fail[j - 1]

        if(dna[i] == dna[j]):
            j += 1

        fail[i] = j


    with open('output/kmp.txt', 'w') as output:
        output.write(' '.join(list(map(str, fail))))

if __name__ == '__main__':
    main()