	
from math import sqrt

# Utility Functions

def normalize_samples(samples):
	fieldsLen = len(samples[0])
	newSamples = [[0]*fieldsLen for k in range(len(samples))]

	for j in range(fieldsLen):
		fieldSet = [0]*len(samples)

		for i in range(len(samples)):
			fieldSet[i] = samples[i][j]

		normSet = norm_arr(fieldSet)

		for i in range(len(samples)):
			newSamples[i][j] = normSet[i]


	return newSamples


# Statistics Functions

"""
float mean(single variable data)
	Returns the mean value of the data
"""
def mean(v_data):
	acum = 0.0
	for val in v_data:
		acum += val

	return acum / len(v_data)

"""
float var(single variable data)
	Returns the variance value of the data and the mean given. If no mean is given
	it calculates the mean from the data first.
"""
def var(v_data, m_data=None):

	if m_data == None:
		m_data = mean(v_data)

	acum = 0.0
	for val in v_data:
		dif = val - m_data
		acum += dif*dif

	return acum / (len(v_data)-1)

"""
float std(single variable data, variance)
	Returns the Standard Deviation value of the variance if given,
	otherwise, it calculuates the variance based on the data
"""
def std(v_data, var_data=None):
	if var_data == None:
		var_data = var(v_data)
	return sqrt(var_data)




"""
float norm_arr(data set)
	Returns the data points normalized by the formula (xi - xmean) stddev
"""
def norm_arr(v_set, vmean=None, vstd=None):
	if vmean == None:
		vmean = mean(v_set)

	if vstd == None:
		vstd  = std(v_set, var(v_set, vmean))

	newSet = [0]*len(v_set)
	for i in range(0, len(v_set)):
		newSet[i] = (v_set[i] - vmean) / vstd

	return newSet


"""
float correlation(x data set, y data set)
	Returns the correlation between the values x and y.
	When correlation -> +1 the variables are highly positive corrleated,
	When correlation -> -1 the variables are highly negative correlated,
	When correlation -> 0  the variables are not correlated
"""
def correlation(xs, ys):
	if len(xs) != len(ys):
		print "Error In Correlation(): Trying to correlate different length datasets for x and y!"
		return

	xs = norm_arr(xs)
	ys = norm_arr(ys)

	corr = 0.0

	for i in range(0, len(xs)):
		corr += xs[i]*ys[i]

	corr = corr / len(xs)

	return corr