#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_path(dir):
  l=[]
  filenames=os.listdir(dir)
  for filename in filenames:
    l.append(os.path.abspath(os.path.join(dir,filename)))
  return l

def copy_to(paths,dir):
#  print paths
 # print dir
  if not os.path.exists(paths):
    os.makedirs(paths)
  src=get_special_path(dir)

  for i in range(0,len(src)):
   shutil.copy(src[i],paths)

def zip_to(paths,zippath):
  l=get_special_path(zippath)
  print 'I am foing to do zip'+paths
  for i in range(0,len(l)):
   cmd='zip -j '+paths+' '+l[0]
   (status,output)=commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
#  print output
  
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
    copy_to(todir,args[0])

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
    zip_to(tozip,args[0])

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  #print args

  # +++your code here+++
  # Call your functions
  #get_special_path(args[0]))
  #print l
  #copy_to()
  
  
if __name__ == "__main__":
  main()
