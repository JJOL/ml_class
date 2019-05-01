import numpy as np
import random as r

def genPawnInputTable(n):
	table = np.zeros((n,n))
	table[r.randrange(n),r.randrange(n)] = 1
	return table

def genPawnOutputTable(inTable):
	outTable = np.array(inTable)
	(n,m) = outTable.shape
	for i in range(n):
		for j in range(m):
			if outTable[i,j] == 1 and i > 0:
				outTable[i,j] = 0
				outTable[i-1,j] = 1

	return outTable

def getPawnDataPair(n):
	inp = genPawnInputTable(n)
	out = genPawnOutputTable(inp)
	return (inp, out)

def genPawnData(n, k):

	data = [ getPawnDataPair(n) for i in xrange(k) ]

	return np.array(data)



def flattenData(data):
	oxs = []
	oys = []

	for i in xrange(len(data)):
		oxs.append(data[i][0].flatten())
		oys.append(data[i][1].flatten())
	return (np.array(oxs), np.array(oys))








