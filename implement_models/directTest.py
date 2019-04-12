import random as r
from math import sqrt


def makeDirSamples(n):

	xs = []
	ys = []

	for i in range(n):

		d1 = r.randrange(90) + 0.0
		d2 = r.randrange(90) + 0.0
		d3 = r.randrange(90) + 0.0
		d4 = r.randrange(90) + 0.0

		xs.append([d1, d2, d3, d4])

		dmean = (d1 + d2 + d3 + d4) / 4.0

		e1 = abs(d1 - dmean)
		e2 = abs(d2 - dmean)
		e3 = abs(d3 - dmean)
		e4 = abs(d4 - dmean)

		ys.append([e1, e2, e3, e4])

	return (xs, ys)

def normDirSamples(xs, ys):

	n = len(xs)
	nxs = [[0]*4 for i in range(n)]
	nys = [[0]*4 for i in range(n)]

	for i in range(n):
		nxs[i][0] = xs[i][0] / 90.0
		nxs[i][1] = xs[i][1] / 90.0
		nxs[i][2] = xs[i][2] / 90.0
		nxs[i][3] = xs[i][3] / 90.0

		nys[i][0] = ys[i][0] / 90.0
		nys[i][1] = ys[i][1] / 90.0
		nys[i][2] = ys[i][2] / 90.0
		nys[i][3] = ys[i][3] / 90.0

	return (nxs, nys)
