'''
http://rosalind.info/problems/lgis/

Given: 
A positive integer n <= 1000 followed by a permutation Pi of length n.

Return: 
A longest increasing subsequence of Pi, followed by a longest decreasing subsequence of Pi.
'''

import sys

def less(x, y):
    return x < y

def greater(x, y):
    return x > y

def find_seq(x, comp):
    n = len(x)
    P = [0] * n
    M = [0] * (n + 1)
    longest = 0

    for i in range(n):
       l = 1
       h = longest
       while l <= h:
           mid = (l + h) >> 1
           if (comp(x[M[mid]], x[i])):
               l = mid + 1
           else:
               h = mid - 1
 
       P[i] = M[l - 1]
       M[l] = i
 
       if (l > longest):
           longest = l
 
    res = []
    k = M[longest]
    for i in range(longest):
        res.append(x[k])
        k = P[k]

    return res[::-1]

def find_subseq(seq):
    max_seq = []
    min_seq = []

    max_seq = find_seq(seq, less)
    min_seq = find_seq(seq, greater)

    with open('output/lgis.txt', 'w') as output:
        output.write(' '.join(list(map(str, max_seq))))
        output.write(' '.join(list(map(str, min_seq))))

def main():
    with open(sys.argv[1], 'r') as data:
        n = int(data.readline())
        seq = map(int, data.readline().split())

    find_subseq(seq)

if __name__ == '__main__':
    main()