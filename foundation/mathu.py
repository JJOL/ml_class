def extendida(mat, n, m):
	cpy = [[0]*(2*m) for k in range(0, n)]

	#Copy Original
	for i in range (0,n):
		for j in range(0,m):
			cpy[i][j] = mat[i][j]

	#Identity Side
	for i in range(0,n):
		cpy[i][i+m] = 1

	return cpy



def invMat(mat, n, m):

	cpy = extendida(mat, n, m)

	if n != m:
		print "N="+str(n)+",M="+str(m)+" Must be equal!"
		return -1

	for j in range(0, m):
		a = cpy[j][j]
		
		for k in range(j, 2*m):
			cpy[j][k] = (1.0/a)*cpy[j][k]

		for i in range(j+1, n):
			b = cpy[i][j]
			for k in range(j, 2*m):
				cpy[i][k] = cpy[i][k] - b*cpy[j][k]

	for j in range(m-1, -1, -1):
		for i in range(j-1, -1, -1):
			b = cpy[i][j]
			for k in range(0, 2*m):
				cpy[i][k] = cpy[i][k] - b*cpy[j][k]


	#Return only Left Inversion
	res = [[0]*m for k in range(n)]

	for i in range(0, n):
		for j in range(0, m):
			res[i][j] = cpy[i][j+n]

	return res


def makeMat(els, n, m):
	mat = [[0]*m for k in range(0,m)]
	c = 0

	if len(els) != n*m:
		print "N="+str(n)+",M="+str(m)+" Are invalid dimesions for " + str(len(els)) + " values!"
		return -1

	for i in range(0, n):
		for j in range(0, m):
			mat[i][j] = els[c]
			c += 1

	return mat

def printMat(mat, n, m):
	for i in range(0, n):
		s = ""
		for j in range(0, m):
			s += str(mat[i][j])
			if j != m-1:
				s += " "
		print s



