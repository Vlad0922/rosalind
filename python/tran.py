'''
http://rosalind.info/problems/tran/

Given: 
Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: 
The transition/transversion ratio R(s1,s2)
'''

import sys

from common import readFASTA

def is_transition(p, q):
    s = ord(p) + ord(q)
    if( (s == ord('A') + ord('G')) or (s == ord('C') + ord('T'))):
        return True
    else:
        return False

def main():
    data = readFASTA(sys.argv[1])

    s, q = [d.dna for d in data]

    transitions = transversions = 0
    for i in range(len(q)):
        if(s[i] != q[i]):
            if(is_transition(s[i], q[i])):
                transitions += 1
            else:
                transversions += 1

    print 1.*transitions/transversions

if __name__ == '__main__':
    main()