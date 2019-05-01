"""
Module: Imgs Renamer
Author: Juan Jose Olivera Loyola
Date: 31/04/19
Description: 
  Simple Files Renamer Helper Script for renaming, (with an indexed format), 
  the files withing a given directory.
  Files keep as extension the suffix after the '.' character in the original name.

Usage: ./python imgs_renamer <directory_path> [custom_format_tag]
Args:
 - directory_path: Absolute or relative path of the directory containing the files.
 - custom_format_tag: Optional. Custom Prefix Tag for each renamed file.

 Example:
 1. Consider directory "ex_dir" with files "Cats.jpg", "Dogs.jpg", "Happy Birds.jpg"
 2. If we were to execute ./python imgs_renamer "ex_dir" "myfiles"
 3. Then we would see in directory "ex_dir" the files named: "myfiles_1.jpg", "myfiles_2.jpg", "myfiels_3.jpg"

"""

import os
import sys
import shutil

# Validate Needed Arguments
if len(sys.argv) < 2:
	print "Error: Need at least 1 argument\a"
	sys.exit()


rdir = sys.argv[1]

# Validate Directory Given Exists
if not os.path.isdir(rdir):
	print "Error: %s is not a valid directory!\a" % rdir
	sys.exit()

# Add Slash Separator
if rdir[len(rdir)-1] != '/':
	rdir = rdir + '/'

# Check for Custom_tag argument
cust_tag = 'f'
if len(sys.argv) > 2:
	cust_tag = sys.argv[2]


# List Files
files = os.listdir(rdir)

print "Renaming Files..."

for i in range(len(files)):
	f = files[i]
	fparts = files[i].split('.')

	ext = fparts[len(fparts)-1]
	name = f[0:(len(f)-len(ext))]

	orig = "%s%s%s" % (rdir, name, ext)
	dest = "%s%s_%i.%s" % (rdir, cust_tag, i, ext)

	print "Moving from " + orig + " to " + dest
	shutil.move(orig, dest)

print "\nRenamed %i files!" % len(files)
print "Done with renaming!"
