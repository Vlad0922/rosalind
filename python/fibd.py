'''
http://rosalind.info/problems/fibd/

Given: Positive integers n<=100 and m<=20m.

Return: The total number of pairs of rabbits that will remain after the nn-th month if all rabbits live for mm months.
'''

import sys

def main():

	with open(sys.argv[1], 'r') as data:
		n, k = map(int, data.read().strip().split())

	young = 1
	mature = 0
	dead = [0]*(n + k - 2)

	for i in range(0, n - 1):
		tmp = young
		young = mature
		mature += tmp

		mature -= dead[i]
		dead[i + k - 1] = tmp		

	print mature + young

if __name__ == '__main__':
    main()