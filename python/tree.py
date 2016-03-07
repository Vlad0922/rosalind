'''
http://rosalind.info/problems/tree/

Given: A positive integer n <= 1000 and an adjacency list corresponding to a graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.
'''

import sys

def main():
	with open(sys.argv[1], 'r') as data:
		n = int(data.readline())
		edges = list()

		for line in data:
			u, v = line.rstrip('\n').split()
			edges.append((u, v))

	print n - len(edges) - 1

if __name__ == '__main__':
    main()
