
"""
Module: C4.5 Tree Building Algorithm Adaptation
Author: Juan Jose Olivera
"""

class Node
	def __init__(self, ctype, index, value, majority):
		self.ctype    = ctype
		self.index    = index
		self.value    = value
		self.majority = majority
		self.isLeaf   = True
		self.children = []
		pass

	def setChildren(self, children):
		self.children = children
		self.isLeaf   = False

	def eval(self, X):
		if self.isLeaf:
			return None

		if self.ctype == 1:
			if X[self.index] < self.value:
				return self.children[0]
			else:
				return self.children[1]
		else:
			return self.children[self.value.index(X[self.index])]

	def getMajority(self):
		return self.majority


class CTree
	
	def __init__(self):
		pass


	def forward(self, X):
		p = n = self.root
		while n != None:
			p = n
			n = n.eval(X)

		return p.getMajority()

	def describeFeatures(self, types, values):
		self.attrTypes = types
		self.attrValues = values

	def extractFeatures(self, dataX):
		# Continous Type for each Feature. 1 continuos. 0 Discrete/Nominal
		self.attrTypes  = []
		# Atribute Values for Discrete Variables
		self.attrValues = [] 

		#for j in xrange(len(dataX[0])):

			#for i in xrange(len(dataX)):


	def evaluate(self, testX, testY):
		pass

	def bestAttrib(self, attributes, dataX, dataY):
		IG = []
		for attrib in attributes:
			IG[attrib] = entropy(dataX, dataY) - 

	def train(self, trainX, trainY, validX, validY, height):

		# Make while there are features for each branch
		root = Node(root, allAttribs)
		root.setData(trainX, trainY)
		stack = list()
		stack.push(root)
		while (!stack.empty()):

			node = stack.pop()
			(nx,ny) = node.getData()
			(attrib, v) = self.bestAttrib(node.attribs, nx, ny)
			newNodes = self.split(node, attrib, v) # Set node attrib index, attrib value
			node.setChildren(newNodes)
			stack.push(newNodes)


			(tp, tn, fp, fn, vErrAcum) = evaluate(validX, validY)


