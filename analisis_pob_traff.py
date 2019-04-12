import csv

top_f = open("top_25_g_f.csv", "rb")

parser = csv.reader(top_f, delimiter=',')

data = []

for row in parser:
	data.append([float(row[3]), float(row[2])])	

import linearregression as lr

model = lr.trainLinearModel(data, 0.01, 0.000005, 6000)