'''
http://rosalind.info/problems/subs/

Given: 
Two DNA strings s and t (each of length at most 1 kbp).

Return: 
All locations of t as a substring of s.
'''

import sys
import re

def main():

	with open(sys.argv[1], 'r') as data:
		s, t = data.readlines()
		s = s.rstrip()
		t = t.rstrip()

	locations = []
	for i in range(0, len(s)-len(t)+1):
	    if s[i:i+len(t)] == t:
	        locations.append(str(i+1))

	print ' '.join(locations)

if __name__ == '__main__':
    main()