import numpy as np

"""
    loadData(fname)
    - Loads data from the csv file fname into a x,y numpy representation
"""

def loadData(fname):
    import csv
    dfile = open(fname, 'rb')
    reader = csv.reader(dfile, delimiter=',')
    data = []
    
    for row in reader:
        data.append(row)

    ndata = np.array(data)
    
    # Buld xSet and ySet
    ys = ndata[1:,1]
    ys = ys.reshape(len(ys),1)
    xs = np.transpose([ndata[1:,2], ndata[1:,4], ndata[1:,5]])
    
    return (xs,ys)

"""
    encode1hotColumn(col, xs, possibles)
    - Replaces column col of xs with a 1 hot encoding made from the values of possibles.
"""
def encode1hotColumn(col, xs, possibles):
    encarr = np.zeros((len(xs),len(possibles)))
    for i in range(len(xs)):
        pos = possibles.index(xs[i,1])
        if pos != -1:
            encarr[i,pos] = 1
        else:
            print "SUPER ERROR! Not Able to Find '"+xs[i,1]+"'"
    xs = np.delete(xs,1,1)
    xs = np.append(xs, encarr, axis=1)
    return xs

"""
    cleanDataFromColumn(col, xs, ys)
    - Removes those data tuples in both xs and ys where value in column col is null or empty or invalid
"""
def cleanDataFromColumn(col, xs,ys):
    missing = []
    (h,w) = xs.shape
    for i in xrange(h):
        if xs[i,col] == '':
            missing.append(i)
    xs = np.delete(xs, missing, 0)
    ys = np.delete(ys, missing, 0)
    return (xs, ys)


"""
    normalizeCol(col, xs)
    - Normalizes values on column col in xs between a range of [0,1] using Min-Max Feature Scaling Normalization
"""
def normalizeCol(col, xs):
    maxFeat = np.amax(xs[:,col])
    minFeat = np.amin(xs[:,col])

    xs[:,col] = (xs[:,col] - minFeat) / (maxFeat - minFeat)
    return xs


def splitData(xs,ys,n):
    trainXs = xs[:n]
    trainYs = ys[:n]
    validXs = xs[n:]
    validYs = ys[n:]
    return (trainXs, trainYs, validXs, validYs)



def crossValidation(model,xs,ys,k):
    for fold in folds:
        



