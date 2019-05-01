"""
Module: Imgs Discriminator
Author: Juan Jose Olivera Loyola
Date: 01/05/19
Description: 
  Simple Files Discriminator Helper Script for dividing a set of files in a given
  directory and placing the discriminated files into a different directory.

Usage: ./python imgs_discriminator <directory_path> <discrim_map_file> [discrim_dest_dir]
Args:
 - directory_path: Absolute or relative path of the directory containing the files.
 - discrim_map_file: File containing a list of file_names to be discriminated out of the original set.
 - discrim_dest_dir: Optional.

 Example:
 1. Consider directory "ex_dir" with files "Cats.jpg", "Dogs.jpg", "Happy Birds.jpg"
    and a Discrimination file "no mammals.txt" with "Cats.jpg" and "Dogs.jpg" in 2 lines
 2. If we were to execute ./python imgs_renamer "ex_dir" "no mammals.txt"
 3. Then we would see in directory "ex_dir" 2 directories "positive" with file "Happy Birds.jpg"
    and "negative" with the files named: "Cats.jpg" and "Dogs.jpg"

"""

import os
import sys
import shutil

# Validate Needed Arguments
if len(sys.argv) < 3:
	print "Error: Need at least 2 arguments!\a"
	sys.exit()


rdir = sys.argv[1]

# Validate Directory Given Exists
if not os.path.isdir(rdir):
	print "Error: %s is not a valid directory!\a" % rdir
	sys.exit()

# Add Slash Separator
if rdir[len(rdir)-1] != '/':
	rdir = rdir + '/'

# Validate Discriminator File
dfilename = sys.argv[2]
if not os.path.isfile(dfilename):
	print "Error: %s is not a valid file!\a" % rdir
	sys.exit()

# Load Discrimination Names
dfile = open(dfilename, "r")

discr_names = dfile.read().split('\n')

dfile.close()


# List Files
files = os.listdir(rdir)

# Making Positive/Negative Dirs
os.mkdir("%spositive" % rdir)
os.mkdir("%snegative" % rdir)

print "Discriminating Files..."

for i in range(len(files)):
	f = files[i]

	orig = "%s%s" % (rdir, f)

	if f in discr_names:
		# Discriminate
		# Move to Negative Dir
		status = 'negative'
	else:
		# Move to Positive Dir
		status = 'Positive'

	dest = "%s%s/%s" % (rdir, status, f)

	print "Moving from " + orig + " to " + dest
	shutil.move(orig, dest)
	

print "\nDiscriminated %i files!" % len(files)
print "Done with renaming!"