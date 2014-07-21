#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  f=open(filename,'r')
  str=f.read()
  match=re.findall(r'GET\s(.*puzzle.*)HTTP',str) 
  l=[]
  b=[]
  for n in match:  #all path in match
    a='http://code.google.com'+n 
    if a not in b:
      b.append(a) # b is google.com
  
  #b.sort()
  return sorted(b,key=lambda s:(re.search(r'-(\w+).jpg',s).group(1))) 
  #return b
def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  for i in range(0,len(img_urls)):
    urllib.urlretrieve(img_urls[i],'img'+str(i)) 
  f=open('index.html','w')
  f.write('<verbatim>\n')
  f.write('<html>\n<body>\n')
  for i in range(0,len(img_urls)):
    path='/home/jacob/python/google/google-python-exercises/logpuzzle/img%d'%(i) 
    f.write('<img src='+path+'>')
  f.write('\n</body>\n</html>')

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
  
 # print todir
 # print args[0]
  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  #else:
   # print '\n'.join(img_urls)

if __name__ == '__main__':
  main()