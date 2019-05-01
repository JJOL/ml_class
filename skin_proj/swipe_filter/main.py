from bottle import get, post, route, request, run, template, static_file
import json

import os
import sys
import shutil

import numpy as np
#from PIL import Image
#print('sys.argv[0] =', sys.argv[0])             
pathname = os.path.dirname(sys.argv[0])        
#print('path =', pathname)
#print('full path =', ) 

## Load Images from Specified Dir
if len(sys.argv) < 2:
	print "Not Enough Arguments Passed!"
	sys.exit()

rdirpath = sys.argv[1]

if not os.path.isdir(rdirpath):
	print "%s is not a valid dir!" % rdirpath
	sys.exit()

imagesArray = os.listdir(rdirpath)
delArr = list()

print "Found %i files in %s" % (len(imagesArray), rdirpath)


def printDelReport():
	print "%i images deleted so far!" % len(delArr)

	parts = rdirpath.split('/')
	fname = "delreport_"+parts[len(parts)-1]+".txt"

	freport = open(fname, "w")
	for img in delArr:
		freport.write("%s\n" % img)
	
	freport.close()


@get('/')
def index():
    return static_file('index.html', os.path.abspath(pathname))

@get('/loadimgs')
def loadImgs():
	a = int(request.params.get('begin'))
	b = int(request.params.get('end'))
	print "Begin: " + str(a)
	print "End: " + str(b)
	
	images = []
	for i in range(a, b):
		iobj = {}
		iobj['iname'] = imagesArray[i]
		iobj['iurl']  = '/img/'+imagesArray[i]
		images.append(iobj)

	return json.dumps(images)
	#return "Error: Not Coded!"

@post('/updateimgs')
def updateImgs():
	a = int(request.params.get('begin'))
	b = int(request.params.get('end'))
	states = request.params.get('states').split('-')

	ind = 0
	for i in range(a, b):
		if (states[ind] == '0'):
			delArr.append(imagesArray[i])
		ind += 1

	printDelReport()

	return "Done!"

@route('/img/<file>')
def serve(file):
	return static_file(file, root=rdirpath)


run(host='localhost', port=8080, debug=True)