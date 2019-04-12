import csv

pob_d = open("estados_pob_f.csv", "rb")
pob_reader = csv.reader(pob_d, delimiter='\t')

data = []

for row in pob_reader:
	data.append( [float(row[1].replace(" ", "")), float(row[2].replace(",",""))] )

import linearregression as lr

lr.trainLinearModel(data, 0.005, 0.000005, 6000)


xs = [data[k][0] for k in range(len(data))]
ys = [data[k][1] for k in range(len(data))]


plt.scatter(xs, ys)
plt.show()