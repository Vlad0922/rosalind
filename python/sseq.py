'''
http://rosalind.info/problems/sseq/

Given: 
Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: 
One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
'''

import sys

from common import readFASTA

def main():
    data = readFASTA(sys.argv[1])
    s, q = [d.dna for d in data]

    i = 0
    res = list()

    for c in q:
        idx = s.find(c, i)

        res.append(idx + 1)
        i = idx + 1

    print ' '.join(list(map(str, res)))

if __name__ == '__main__':
    main()