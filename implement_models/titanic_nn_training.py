import data_utils as dutils

(xs,ys) = dutils.loadData('train.csv')
xs = dutils.encode1hotColumn(1, xs, ['male','female'])
(xs,ys) = dutils.cleanDataFromColumn(1, xs, ys)

xs = xs.astype('float32')
ys = ys.astype('float32')

xs = dutils.normalizeCol(1, xs)
xs = dutils.normalizeCol(0, xs)

(trainXs, trainYs, validXs, validYs) = dutils.splitData(xs, ys, 550)

import neuralnet as nn

nnet = nn.NeuralNet(4)
nnet.addLayer(4)
nnet.addLayer(2)
nnet.addLayer(1)

(terr, verr) = nnet.train('m', trainXs.tolist(), trainYs.tolist(), 
							   validXs.tolist(), validYs.tolist(), 
							   1500, 0.2)

nn.show_errorGraph('Neural Net', (terr, verr))