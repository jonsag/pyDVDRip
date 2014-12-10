#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Encoding: UTF-8

import getopt, sys

from misc import *

##### handle arguments #####
try:
    myopts, args = getopt.getopt(sys.argv[1:], 'p:o:hv' ,
                                 ['path=',
                                  'out',
                                  'help',
                                  'verbose'])

except getopt.GetoptError as e:
    onError(1, str(e))

if len(sys.argv) == 1:  # no options passed
    onError(2, 2)

path = "."
out = ""
verbose = False

for option, argument in myopts:
    if option in ('-p', '--path'):
        path = argument
    elif option in ('-o', '--out'):
        out = argument
    elif option in ('-h', '--help'):
        usage(0)
    elif option in ('-v', '--verbose'):
        verbose = True
       
if path and not os.path.isdir(path):
    onError(3, path)
elif path and not os.path.isdir(os.path.join(path, "VIDEO_TS")):
    onError(4, path)
    
if not out:
    onError(5, 5)
    
shripCommands = setCommands(path, verbose)
shripListTitles, shripListAudio, shripListChapters, shripListSubtitles, shripEncode = shripCommands

