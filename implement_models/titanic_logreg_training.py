import data_utils as dutils

(xs,ys) = dutils.loadData('train.csv')
xs = dutils.encode1hotColumn(1, xs, ['male','female'])
(xs,ys) = dutils.cleanDataFromColumn(1, xs, ys)

xs = xs.astype('float32')
ys = ys.astype('float32')

xs = dutils.normalizeCol(1, xs)
xs = dutils.normalizeCol(0, xs)

(trainXs, trainYs, validXs, validYs) = dutils.splitData(xs, ys, 550)

import logistic_classif as logist

logmodel = logist.LogisticClassifier(4)

logmodel.train(trainXs.tolist(), trainYs.tolist(), 1500, 0.1)


print "For Male, Low Class, and 30s"
print logmodel.forward([1, .31, 1, 0])

print "For Female, High Class, and 30s"
print logmodel.forward([0, .31, 0, 1])
#(terr,verr) = logist.train(logmodel, trainXs.tolist(), trainYs.tolist(), validXs.tolist(), validYs.tolist())

#logmodel.save('titanic_logistic.net')

#import neuralnet as nn
#nn.show_errorGraph('Logistic Training', (terr,verr))