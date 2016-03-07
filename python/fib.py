'''
http://rosalind.info/problems/fib/

Given: 
Positive integers n<=40 and k<=5.

Return: 
The total number of rabbit pairs that will be present after nn months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of kk rabbit pairs (instead of only 1 pair).
'''

import sys

def main():

	with open(sys.argv[1], 'r') as data:
		n, k = map(int, data.read().strip().split())

	young = 1
	mature = 0

	for i in range(0, n - 1):
		tmp = young
		young = mature * k
		mature += tmp

	print mature + young

if __name__ == '__main__':
    main()