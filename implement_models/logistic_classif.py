import random as r
import math

class LogisticClassifier():
	def __init__(self, dimen):
		self.dimen = dimen
		self.createModel()

	def save(self, fname):
		fOut = open(fname, "w")
		fOut.write(fname+"\n")
		fOut.write(str(self.xDimens)+" ") # Write Input Dimension
		
		pass
	def load(self, fname):
		pass

	def getCrossEntropy(self, xs, ys):
		errorAcum = 0.0
		for i in xrange(len(xs)):
			y = ys[i][0]
			h = self.forward(xs[i])

			if y == 1:
				if h == 0:
					h = 0.00001
				error =  (-1)*math.log(h)
			else:
				if h == 1:
					h = 0.99999
				error = (-1)*math.log(1 - h)

			errorAcum += error

		errorAcum /= len(xs)

		return errorAcum
		

	def createModel(self):
		self.params = [r.uniform(-1, 1) for i in xrange(self.dimen + 1)]

	def sig(self, x):
		return 1.0 / (1 + math.exp(-x))

	def forward(self, X):
		linearSum = 0.0
		linearSum += self.params[0]
		for i in xrange(1, len(self.params)):
			linearSum += self.params[i]*X[i-1]

		return self.sig(linearSum)

	def gd(self, xs, ys, lrate):
		temp = list(self.params)

		for j in xrange(len(self.params)):
			dcost = 0.0
			for i in xrange(len(xs)):
				if j == 0:
					dcost += (self.forward(xs[i]) - ys[i][0])
				else:
					dcost += (self.forward(xs[i]) - ys[i][0]) * xs[i][j-1]
			dcost /= len(xs)

			temp[j] -= lrate*dcost
		
		return temp

	def train(self, trainXs, trainYs, epochs, learnRate):
		for e in xrange(epochs):
			errorAcum = 0.0
			
			newParams = self.gd(trainXs, trainYs, learnRate)

			self.params = newParams

			error = self.getCrossEntropy(trainXs, trainYs)

			print "Epoch #" + str(e) + " - Error: " + str(error)


