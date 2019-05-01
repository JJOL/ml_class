from PIL import Image
import numpy as np
import os


# From Stackoverflow user Josh Bleecher Snyder https://stackoverflow.com/questions/4601373/better-way-to-shuffle-two-numpy-arrays-in-unison
def shuffle_in_unison_scary(a, b):
    rng_state = np.random.get_state()
    np.random.shuffle(a)
    np.random.set_state(rng_state)
    np.random.shuffle(b)

def loadImageAsNp(imgpath, isize=224):
	im = Image.open(imgpath)
	im = im.resize((isize,isize))
	im = im.convert(mode='RGB')
	imgdata = np.array(list(im.getdata()))
	imgdata = np.array(np.split(imgdata, isize))
	return imgdata

# Load Images and Convert them to 224x224
DIR = 'downloads/Vitiligo/'
PS_DIR = DIR + 'positive'
NG_DIR = DIR + 'negative'

ps_files = os.listdir(PS_DIR)
ng_files = os.listdir(NG_DIR)

# Get Labels
ps_labels = np.ones(len(ps_files))
ng_labels = np.zeros(len(ng_files))
labels = np.append(ps_labels, ng_labels)

size = len(labels)

image_data = np.zeros((size, 224, 224, 3))

i = 0
for i in xrange(len(ps_labels)):
	print "Loading PS Image (%i)" % i
	# im = Image.open(PS_DIR+'/'+ps_files[i])
	# im = im.resize((224,224))
	# im = im.convert(mode='RGB')
	# imgdata = np.array(list(im.getdata()))
	# imgdata = np.array(np.split(imgdata, 224))

	image_data[i] = loadImageAsNp(PS_DIR+'/'+ps_files[i])

for j in xrange(len(ng_labels)):
	print "Loading NG Image (%i)" % j
	# im = Image.open(PS_DIR+'/'+ng_files[j])
	# im = im.resize((224,224))
	# im = im.convert(mode='RGB')
	# imgdata = np.array(list(im.getdata()))
	# imgdata = np.array(np.split(imgdata, 224))

	image_data[i] = loadImageAsNp(NG_DIR+'/'+ng_files[j])

#image_data = np.array(image_data)
print image_data.shape

shuffle_in_unison_scary(image_data, labels)
print "Shuffled!"



# Load Vitilogo Images -> 224x224x3 numpy array
# Numpy Array -> Vector Labels YES/NO

#print "We have %i data" % len(img_data)
print "We have %i labels" % len(labels)


