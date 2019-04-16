

def sgd():
	pass

def bgd():
	pass


class StrategicLearner:
	
	def __init__(self):
		self.batch_size = 0
		self.gdType = 'b'  # Default BGD

		self.lrStrat = 'f' # Fixed Learning Rate
		self.learningRate = 0.05 # Init Default Learning Rate


	def splitDataSet(self, dataSet):
		trainSet = []
		validSet = []
		return (trainSet, validSet)

	def train(self, model, trainSet, validSet, epochs):
		for ep in xrange(epochs):

			gd = self.getGDFunc()
			def errorCorrect():
				
				pass
			gd(errorCorrect)

			for i in xrange(len(trainSet)):
				pass

		print "Epoch #"+str(ep)

	def evaluate(self, model, testSet):
		pass

	"""
	Batch Gradient Descent
	- Makes a complete run through train data before updating parameters
	"""
	def setBGD(self):
		self.gdType = 'b'
	"""
	Stochastic Gradient Descent
	- Updates parameters for each data processed
	- May be very wild (stochastic)
	"""
	def setSGD(self):
		self.gdType = 's'
	"""
	Mini-Batch Gradient Descent
	- Divides Test Data into Mini Batches. Updates parameters after each minibatch
	"""
	def setMGD(self, batch_size):
		self.gdType = 'm'
		self.batch_size = batch_size