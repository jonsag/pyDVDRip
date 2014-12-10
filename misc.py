#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Encoding: UTF-8

import ConfigParser, os, sys

config = ConfigParser.ConfigParser()
config.read("%s/config.ini" % os.path.dirname(os.path.realpath(__file__)))  # read config file

scores = int(config.get('decoration', 'scores'))

shripPath = config.get('ogmrip', 'shripPath')

spokenLanguages = config.get('ogmrip', 'spokenLanguages')
subLanguages = config.get('ogmrip', 'subLanguages')

def onError(errorCode, extra):
    print "\nError:"
    if errorCode == 1:
        print extra
        usage(errorCode)
    elif errorCode == 2:
        print "No options given"
        usage(errorCode)
    elif errorCode == 3:
        print "%s is not a valid path" % extra
        sys.exit(errorCode)
    elif errorCode == 4:
        print "%s does not contain a VIDEO_TS folder" % extra
        sys.exit(errorCode)
    elif errorCode == 5:
        print "You did not set outfile, -o"
        sys.exit(5)
        
def usage(exitCode):
    print "\nUsage:"
    print "-"  * scores
    print "%s -p <path>" % sys.argv[0]
    print "  OR"
    print "%s -h" % sys.argv[0]
    print "    Prints this"
    
def setCommands(path, verbose):
    config.set('ogmrip', 'path', path)
    
    shripListTitles = config.get('ogmrip', 'shripListTitles')
    shripListAudio = config.get('ogmrip', 'shripListAudio')
    shripListChapters = config.get('ogmrip', 'shripListChapters')
    shripListSubtitles = config.get('ogmrip', 'shripListSubtitles')
    shripEncode = config.get('ogmrip', 'shripEncode')
    
    if verbose:
        print "Commands:"
        print shripListTitles
        print shripListAudio
        print shripListChapters
        print shripListSubtitles
        print shripEncode
        
    return (shripListTitles, shripListAudio, shripListChapters, shripListSubtitles, shripEncode)
    
