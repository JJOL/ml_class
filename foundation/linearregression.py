# http://mccormickml.com/2014/03/04/gradient-descent-derivation/
# https://blog.goodaudience.com/gradient-descent-for-linear-regression-explained-7c60bc414bdd


import random as r
import math
import stats

class LinearModel():

	def __init__(self, params, err, means, stds):
		self.params = params
		self.amean  = means
		self.astd   = stds

		self.error  = err

	def norm(self, sample):
		nSample = list(sample)
		for j in range(len(self.params)-1):
			nSample[j] = (nSample[j] - self.amean[j]) / self.astd[j]
		
		return nSample

	def pred_raw(self, sample):
		h = 0
		
		for i in len(self.params):
			h += sample[i]*self.params[i]

		return h

	def pred(self, sample):
		#norm sample
		sample = self.norm(sample)
		#add bias
		sample = [1] + sample

		return self.pred_raw(sample)



def linearPredict(sample, model):
	pred = 0
	for i in range(0, len(model)):
		pred += model[i]*sample[i]

	return pred

def res(sample):
	return sample[len(sample)-1]

def evalLinearErr(samples, model):
	acum_error = 0
	for sample in samples:
		pred = linearPredict(sample, model)
		l_error = math.pow(pred-res(sample), 2)
		#print "Error for sample: "+str(l_error)
		acum_error += l_error

	return acum_error / (len(samples))

def gd(samples, model, learningRate):
	
	newModel = list(model)

	for j in range(0, len(model)):
		#gradient cost derivative
		dcost = 0
		for sample in samples:
			dcost += (linearPredict(sample, model) - res(sample))*sample[j]
		dcost /= len(samples)

		newModel[j] -= learningRate*dcost

	return newModel


def normalizeSamples(samples):
	# Extract Only Features X
	ys = [0]*len(samples)
	xs = [[] for k in range(len(samples))]
	for i in range(len(samples)):
		sample = samples[i]
		ys[i] = sample[len(sample)-1]
		xs[i] = sample[0:len(sample)-1]

	print "Normalizing:"
	print xs
	xs = stats.normalize_samples(xs)

	for i in range(len(xs)):
		xs[i] = xs[i] + [ys[i]]

	return xs

def addBiasAttr(samples):
	return [([1]+sample) for sample in samples]

def generateModel(samples):
	return [r.randrange(0,10) for k in range(0,len(samples[0])-1)]


def trainLinearModel(samples, lrate, errorTol, maxSteps):

	samples = normalizeSamples(samples)
	samples = addBiasAttr(samples)
	model   = generateModel(samples)

	epoch = 1
	prevError = 1000
	error = 100

	__errors__ = []

	while True:
		prevError = error
		oldmodel = model
		model = gd(samples, model, lrate)
		error = evalLinearErr(samples, model)

		print "Epoch("+str(epoch)+") - Error: " + str(error)

		__errors__.append(error)

		epoch += 1

		if oldmodel == model or error < errorTol or epoch > maxSteps:
			break

	print "Done Training!"

	import matplotlib.pyplot as plt
	plt.plot(__errors__)
	plt.show()

	return model


# def trainLinearModel(samples, lrate, errorTol, maxSteps):

# 	samples = normalizeSamples(samples)
# 	samples = addBiasAttr(samples)
# 	model   = generateModel(samples)

# 	epoch = 1
# 	prevError = 1000
# 	error = 100

# 	__errors__ = []

# 	while True:
# 		prevError = error
# 		oldmodel = model
# 		model = gd(samples, model, lrate)
# 		error = evalLinearErr(samples, model)

# 		print "Epoch("+str(epoch)+") - Error: " + str(error)

# 		__errors__.append(error)

# 		epoch += 1

# 		if oldmodel == model or error < errorTol or epoch > maxSteps:
# 			break

# 	print "Done Training!"

# 	import matplotlib.pyplot as plt
# 	plt.plot(__errors__)
# 	plt.show()

# 	lmodel = LinearModel(model, )

# 	return model


# csvfile = open('top_25_g_f.csv', 'rb')
# csvr = csv.reader(csvfile, delimiter=',')


