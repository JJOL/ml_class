"""
	Author: Juan Jose Olivera
	Module: Vanilla-Really-Simple-And-Unoptimized-Neural Network
	
	Objective: To understand and implement a general neural network that is trained with
			   backpropagation on training data, and that it can make predictions.
	Overview: NeuralNet Class
	 - NeuralNet(xDimension) Creates an Empty Neural Network with an input dimension of xDimension
	 - addLayer(n) Adds a layer of n neurons all connected to the previous layer (or input).
	 - forward(x) Makes a 'y' prediction on the input data 'x'
	 - train(xs, ys, epochs, lrate, tol=0.005) Trains the NN Model with the data (xs,ys), a 
	 - learning rate of lrate and for maximum epochs or until the error is less than tol.
	 - save(fname) Saves the network neurons information and metadata into a file named 'fname'
	 - load(fname) Loads the network neurons and metadata from the file named 'fname'
"""



import math
import random as r
import numpy as np

import matplotlib.pyplot as plt

class NeuralNet:
	def __init__(self, xDimens, neurons=None):

		self.xDimens = xDimens
		self.neurons = []
		self.aneurons = []

		if (neurons != None):
			self.neurons = neurons

	def save(self, fname):

		fOut = open(fname, "w")

		fOut.write(fname+"\n")

		fOut.write(str(self.xDimens)+" ") # Write Input Dimension
		fOut.write(str(len(self.neurons[len(self.neurons)-1]))+"\n") # Write Output Dimension

		nlayers = len(self.neurons)
		fOut.write(str(nlayers)+"\n")
		for i in range(nlayers):
			nneurons = len(self.neurons[i])
			nparams  = len(self.neurons[i][0])
			fOut.write(str(nneurons)+" "+str(nparams)+"\n")
			for j in range(nneurons):
				for k in range(nparams):
					fOut.write(str(self.neurons[i][j][k]))
					if k != nparams-1:
						fOut.write(" ")
				fOut.write("\n")

		fOut.close()


	def load(self, fname):
		fIn = open(fname, "r")

		fIn.readline() # Read Name

		sdims = fIn.readline()[:-1].split(' ') # Read Dimensions
		self.xDimens = int(sdims[0])
		self.neurons  = []
		self.aneurons = []

		nlayers = int(fIn.readline()[:-1])

		for i in range(nlayers):
			strLParams = fIn.readline()[:-1].split(' ')
			nneurons = int(strLParams[0])
			nparams  = int(strLParams[1])

			self.addLayer(nneurons)

			for j in range(nneurons):
				sparams = fIn.readline()[:-1].split(' ')

				for k in range(nparams):
					self.neurons[i][j][k] = float(sparams[k])

		fIn.close()



	def addLayer(self, nAmount):

		layer = []
		alayer = []

		nWeights = self.xDimens
		if len(self.neurons) > 0:
			nWeights = len(self.neurons[len(self.neurons)-1])

		for i in range(nAmount):
			neuron = [ r.uniform(-1, 1) for k in range(nWeights+1)]
			layer.append(neuron)
			alayer.append(0)

		# self.neurons.append(layer)
		self.aneurons.append(alayer)
		self.neurons.append(layer)

		# self.neurons.append(np.array(layer))

	def sig(self, x):
		return 1.0 / (1.0 + math.exp(-x))


	def forward(self, X):

		# print "On Forward()"
		# prevValues = np.array(X)
		prevValues = X
		neurons = self.neurons

		# print "X"
		# print prevValues

		# For each Layer
		for i in xrange(len(neurons)):
			lOutput = []
			# For each Neuron
			for j in xrange(len(neurons[i])):
				# For each Weigh
				nRes = neurons[i][j][0] # Start With Bias
				for k in xrange(1, len(neurons[i][j])):
					# print "Neurons: "
					# print neurons
					# print "PrevValues: "
					# print prevValues
					nRes += neurons[i][j][k] * prevValues[k-1]

				# Pass Linear Sum through Squification funtion sigmoid
				actValue = self.sig(nRes)
				self.aneurons[i][j] = actValue

				lOutput.append(actValue)

			prevValues = lOutput

			# prevValues = neurons[i] @ prevValues
			


		return prevValues

	def emptyParamsCopy(self):
		ncopy = [[] for k in xrange(len(self.neurons))]

		for i in xrange(len(self.neurons)):
			ncopy[i] = [[] for k in xrange(len(self.neurons[i]))]

			for j in xrange(len(self.neurons[i])):
				ncopy[i][j] = [0]*len(self.neurons[i][j])

		return ncopy

	def emptyNeuronsCopy(self):
		ncopy = [[] for k in xrange(len(self.neurons))]

		for i in xrange(len(self.neurons)):
			ncopy[i] = [0]*len(self.neurons[i])

		return ncopy


	def BP(self, x, y, avalues, _neurons):

		neurons = self.emptyParamsCopy()
		for i in xrange(len(neurons)):
			for j in xrange(len(neurons[i])):
				for k in xrange(len(neurons[i][j])):
					neurons[i][j][k] = _neurons[i][j][k]

		sGrad = self.emptyParamsCopy()
		deltas = self.emptyNeuronsCopy()

		# Append X layer as bottom delta L+1 layer
		avalues = [x] + avalues

		# Trick Adding An Extra Final Neuron to be able to apply our recursive formula
		# - This is necessary as for getting for each neuron, the dError/dNeuron we need
		# - to get the upper neurons diff and weights. So for the last layer, we need to invent
		# - a new layer.

		# Delta0 = 1
		deltas.append([1.0])

		# New Neuron with 0 Bias and Weights equal to the derivative of error regarding each
		# last layer neuron
		lastLayer = len(avalues)-1
		neu0 = [0.0]
		for j in xrange(len(avalues[lastLayer])):
			neu0.append(avalues[lastLayer][j] - y[j])
		neurons.append([neu0])

		# print "New Neuron: "
		# print neu0

		# print "Deltas: "
		# print deltas

		# print "Activations: "
		# print avalues

		# Do Back Propagation
		for i in xrange(len(avalues)-1):
			l = len(avalues) - i - 1
			for j in xrange(len(avalues[l])):

				dOutNeuron = 0.0
				# print "Calculating dC/dN for Neuron (" + str(l) + "," + str(j) + ")"
				# print "Current Layer "+str(l-1)+" Neurons Amount: " + str(len(avalues[l]))
				# print "Deltas: "
				# print deltas
				# print "Upper Layer "+str((l-1)+1)+" Neurons Amount: " + str(len(deltas[l-1+1]))

				for jj in xrange(len(deltas[l-1+1])):
					# print "N"+str(jj)
					# print "Upper Neuron ("+str(l-1+1)+","+str(jj)+") has " + str(len(neurons[l-1+1][jj])-1) + " weights" 
					dOutNeuron += deltas[l-1+1][jj] * neurons[l-1+1][jj][j+1]

				# print "DOutNeuron: " + str(dOutNeuron)

				dltInNeuron = dOutNeuron * (avalues[l][j] * (1 - avalues[l][j]))
				deltas[l-1][j] = dltInNeuron



				# For Bias
				sGrad[l-1][j][0] = dltInNeuron

				# For Every Parameter
				for k in xrange(1, len(neurons[l-1][j])):
					sGrad[l-1][j][k] = dltInNeuron * avalues[l-1][k-1]

		return sGrad
					


	def sumGradients(self, tGradients, sGradient):
		for i in xrange(len(tGradients)):
			for j in xrange(len(tGradients[i])):
				for k in xrange(len(tGradients[i][j])):
					tGradients[i][j][k] += sGradient[i][j][k]

	def averageGradients(self, gradients, n):
		for i in xrange(len(gradients)):
			for j in xrange(len(gradients[i])):
				for k in xrange(len(gradients[i][j])):
					gradients[i][j][k] /= n

	def applyGradient(self, gradients, lRate):
		# For Every Layer
		for i in xrange(len(self.neurons)):
			# For Every Neuron in the Layer
			for j in xrange(len(self.neurons[i])):
				# For Every Paramter of the Neuron
				for k in xrange(len(self.neurons[i][j])):
					self.neurons[i][j][k] -= lRate*gradients[i][j][k]

	def BGD(self, trainSet, trainYs, validSet, validYs,epochs, learnRate, tolerance):
		step = 0
		validErrorAcum = 100

		trainErrors = []
		validErrors = []

		for e in xrange(epochs):

			step += 1
			grads = self.emptyParamsCopy()

			trainErrorAcum = 0

			for i in xrange(len(trainSet)):
				# print "Testing with X"
				# print trainSet[i]
				pred = self.forward(trainSet[i])
				error = 0
				for j in xrange(len(pred)):
					error += math.pow(pred[j]-trainYs[i][j], 2)

				trainErrorAcum += error

				sampGrad = self.BP(trainSet[i], trainYs[i], self.aneurons, self.neurons)

				# print "Gradient for Sample"
				# print sampGrad

				self.sumGradients(grads, sampGrad)

				# print "Total Gradient"
				# print grads

			trainErrorAcum /= len(trainSet)
			trainErrors.append(trainErrorAcum)


			validErrorAcum = 0
			for i in xrange(len(validSet)):
				valdata = validSet[i]
				pred = self.forward(valdata)
				error = 0
				for j in xrange(len(pred)):
					error += math.pow(pred[j]-validYs[i][j], 2)
				validErrorAcum += error

			validErrorAcum /= len(validSet)
			validErrors.append(validErrorAcum)

			self.averageGradients(grads, len(trainSet))
			self.applyGradient(grads, learnRate)

			

			print "Epoch #" + str(step) + " - Train Error: " + str(trainErrorAcum) + " - Valid Error: " + str(validErrorAcum)


			if (validErrorAcum <= tolerance):
				break

		return (trainErrors, validErrors)

	def shuffle(self, dataSet, ys):
		for i in xrange(len(dataSet)):
			ri = r.randrange(len(dataSet))
			temp = dataSet[i]
			dataSet[i] = dataSet[ri]
			dataSet[ri] = temp
			temp = ys[i]
			ys[i] = ys[ri]
			ys[ri] = temp


	def gen_batches(self, dataSet, ys, batch_size):
		

		count = 0
		batch = [[],[]]
		batches = []
		for i in range(len(dataSet)):
			# Push Sample to Batch

			batch[0].append(dataSet[i])
			batch[1].append(ys[i])

			count += 1
			if count % batch_size == 0:
				count = 0
				# Push Batch to Batches
				batches.append(batch)
				batch = [[],[]]

		return batches
		


	def MiniGD(self, trainSet, ys, validSet, validYs, epochs, batch_size, learnRate, tolerance=0.005):
		step = 0
		validErrorAcum = 100

		trainErrors = []
		validErrors = []

		for e in xrange(epochs):

			step += 1

			tSuccCount = 0.0
			trainErrorAcum = 0
			self.shuffle(trainSet, ys)
			batches = self.gen_batches(trainSet, ys, batch_size)
			for batch in batches:
				# print "Testing with X"
				# print trainSet[i]
				grads = self.emptyParamsCopy()

				for i in xrange(len(batch[0])):

					pred = self.forward(batch[0][i])
					error = 0
					flawless = 1
					for j in xrange(len(pred)):
						error += math.pow(pred[j]-batch[1][i][j], 2)
						if (pred[j] >= 0.5 and batch[1][i][j] < 0.5) or (pred[j] < 0.5 and batch[1][i][j] >= 0.5):
							flawless = 0

					trainErrorAcum += error
					if flawless:
						tSuccCount += 1

					sampGrad = self.BP(batch[0][i], batch[1][i], self.aneurons, self.neurons)

					# print "Gradient for Sample"
					# print sampGrad

					self.sumGradients(grads, sampGrad)

				self.averageGradients(grads, len(batch[0]))
				self.applyGradient(grads, learnRate)

				# print "Total Gradient"
				# print grads
			trainErrorAcum /= len(trainSet)
			trainErrors.append(trainErrorAcum)



			vSuccCount = 0.0
			validErrorAcum = 0
			tp = 0
			tn = 0
			fp = 0
			fn = 0
			for i in xrange(len(validSet)):
				valdata = validSet[i]
				pred = self.forward(valdata)
				error = 0
				flawless = 1
				for j in xrange(len(pred)):
					error += math.pow(pred[j]-validYs[i][j], 2)
					if (pred[j] >= 0.5 and validYs[i][j] >= 0.5):
						vSuccCount += 1
						tp += 1
					elif (pred[j] < 0.5 and validYs[i][j] < 0.5):
						vSuccCount += 1
						tn += 1
					elif (pred[j] >= 0.5 and validYs[i][j] < 0.5):
						fp += 1
					else:
						fn += 1
				validErrorAcum += error
				#if flawless:
				#	vSuccCount += 1

			validErrorAcum /= len(validSet)
			validErrors.append(validErrorAcum)

			

			tAcc = tSuccCount / len(trainSet)
			vAcc = vSuccCount / len(validSet)

			print "Epoch #" + str(step) + " - Train Error: " + str(trainErrorAcum) + " - Valid Error: " + str(validErrorAcum)
			print "Epoch #" + str(step) + " - Train Accuracy: " + str(tAcc)
			print "Epoch #" + str(step) + " - Valid Accuracy: " + str(vAcc)

			if e == epochs-1:
				print "      T      F"
				print "   ---------------"
				print "P1 |  " + str(tp) + "  |  " + str(fp) + "  |"
				print "   ---------------"
				print "P0 |  " + str(fn) + "  |  " + str(tn) + "  |"
				print "   ---------------"

			if (validErrorAcum <= tolerance):
				break

		return (trainErrors, validErrors)



	def train(self, gtype, testSet, ys, validSet, validYs, epochs, learnRate, tolerance=0.005):
		if gtype=='b':
			return self.BGD(testSet, ys, validSet, validYs, epochs, learnRate, tolerance)
		elif gtype=='m':
			return self.MiniGD(testSet, ys, validSet, validYs, epochs, 50, learnRate, tolerance)
		else:
			print "Unknown Gradient Descent Option!"
			return 0

				


"""
	SubModule: Samples Utility
	Objective: Facilitate the generation, storage and loading of training samples for the Neural Networks
	Overview:
		Main Utility Funcitons:
		 - saveSampels(fname, xs, ys) Saves the samples (xs, ys) into a file named "fname"
		 - loadSamples(fname) Loads the samples (xs, ys) from the file named "fname"
"""
def saveSamples(fname, xs, ys):
	fOut = open(fname, "w")

	n  = len(xs)
	xn = len(xs[0])
	yn = len(ys[0])

	fOut.write(str(n)+"\n")
	fOut.write(str(xn)+" "+str(yn)+"\n")

	for i in range(n):
		for j in range(xn):
			fOut.write(str(xs[i][j])+" ")
		for j in range(yn):
			fOut.write(str(ys[i][j]))
			if j != yn-1:
				fOut.write(" ")

		fOut.write("\n")

	fOut.close()

def loadSamples(fname):
	fIn = open(fname, "r")

	n = int(fIn.readline()[:-1])
	dims = fIn.readline()[:-1].split(' ')
	xn = int(dims[0])
	yn = int(dims[1])

	xs = [[0 for j in range(xn)] for i in range(n)]
	ys = [[0 for j in range(yn)] for i in range(n)]

	for i in range(n):
		sdata = fIn.readline()[:-1].split(' ')

		c = 0
		for j in range(xn):
			xs[i][j] = float(sdata[c])
			c += 1
		for j in range(yn):
			ys[i][j] = float(sdata[c])
			c += 1

	fIn.close()

	return (xs, ys)




# TEST SAMPLES ABOUT GRADES. x >= 0.70 => y=1, x < 0.70 => y=0
def makeGradSamples(n):
	xs = []
	ys = []

	for i in range(n):
		v = r.randrange(100) / 100.0

		xs.append([v])

		if v >= 0.7:
			ys.append([1])
		else:
			ys.append([0])

	return (xs, ys)



def show_errorGraph(title, (terr, verr)):
	x_axis = range(1, len(terr)+1)
	plt.plot(x_axis, terr, 'b', label='Training Error')
	plt.plot(x_axis, verr, 'r', label='Validation Error')
	plt.title(title)
	plt.legend()
	plt.show()