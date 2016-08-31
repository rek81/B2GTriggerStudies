#!/usr/bin/env python
"""
This is a CMSSW tool to help manipulate hlt menus.

It takes an hlt menu as input, creates a new trigger path by cloning a base path, applies
requested module parameter changes on the new path, and writes out the menu.

It is intended to be CMSSW release independent

For additional information, visit the openHLT twiki page
https://twiki.cern.ch/twiki/bin/view/CMS/NewOpenHLT
"""

import argparse

# ---------- configure script with command line options
hlt_ifile="hlt.py"
hlt_ofile="myhlt.py"

verbose=2
# 0: quiet 1: normal 2: debug

appendepilogue=False
# http://docs.python.org/2/library/argparse.html
parser = argparse.ArgumentParser(description='This is a CMSSW tool to clone, modify and add a trigger path back into an HLT menu')


parser.add_argument('-i', '--input-hlt-menu', action='store', metavar='FILE', #type=str,
                    default=hlt_ifile,
                    #required=True,
                    help="name of the base hlt configuration file")

parser.add_argument('-o', '--output-hlt-menu', action='store', metavar='FILE', #type=str,
                    default=hlt_ofile,
                    #required=True,
                    help="name of the hlt configuration file which will have the new path")

parser.add_argument('-p', '--base-trigger-path', action='store', metavar='NAME', #type=str,
                    default="",
                    required=True,
                    help="name of an existing trigger path you want to study")

parser.add_argument('-c', '--trigger-path-changes', nargs='+', action='store', metavar='CHANGES', #type= str,
                    default="",
                    required=True,
                    help='a space seperated list of strings describing the changes to the base trigger path. example: "hltEightJet35eta3p0L1FastJet.MinPt = cms.double(60.0)"')

parser.add_argument('-r', '--rename', action='store', metavar='NAME',#type= bool,
                    default="",
                    help='this name will be appended to the name of the current trigger')

parser.add_argument('-v', '--verbose', action='store', metavar='LEVEL',#type= bool,
                    default=verbose,
                    help='set the verbosity level: 0:quiet, 1:normal, 2:debug (default='+str(verbose)+')')

args = parser.parse_args()
hlt_ifile=args.input_hlt_menu
hlt_ofile=args.output_hlt_menu
verbose=int(args.verbose)
basepath=args.base_trigger_path
changes=args.trigger_path_changes
renaming = args.rename

if verbose:
    print "base HLT menu:", hlt_ifile
    print "trigger path:", basepath
    print "requested changes:", changes
# ------- script configuration ends here


# try and import the necessary modules
import os, sys, hashlib
from datetime import datetime
#if sys.version_info < (2, 7):
#    import CloneTrigger_52x as CloneTrigger
#else:
import CloneTrigger
       
try: import FWCore.ParameterSet.Config as cms
except ImportError:
    print 'Cannot import CMSSW python modules. Did you forget to "cmsenv"?'
    sys.exit()

if verbose==2: print "importing base menu ("+hlt_ifile+")",
hlt_module=hlt_ifile
if hlt_module[-3:] == ".py": hlt_module=hlt_module[:-3]
print hlt_module
try: hlt=__import__(hlt_module)
except ImportError:
    print "\nbase menu import failed"
    print "Cannot load python module:", args.input_hlt_menu
    sys.exit()
if verbose==2: print ": ok"

#http://cmslxr.fnal.gov/lxr/source/FWCore/ParameterSet/python/Config.py#100
process=hlt.process

# Accept shorter "change strings"
changes=[]

for change in args.trigger_path_changes:
    if change[:8] != "process.": change="process."+change
    changes.append(change)
   

#http://cmslxr.fnal.gov/lxr/source/FWCore/ParameterSet/python/SequenceTypes.py#336
newpath=CloneTrigger.clone_path(process, basepath, changes, renaming, verbose==2)

#add the cloned path to the CMSSW process
hash = hashlib.md5( basepath+'\n'.join(changes) ).hexdigest().capitalize()

newpathname=basepath.split("_v")[0]+"_"+renaming+"_v1"

if verbose==2: print "adding new path to the process:",newpathname
process.__dict__[newpathname]=newpath
#FIXME: should I also call  process._insertPaths?
newpath._placeImpl(newpathname,process)

if verbose:
    print "\nPaths in the menu:\n----------------------"
    for key in process.__dict__.keys():
        if  isinstance(process.__dict__[key], cms.Path):
            print key
    print "----------------------\n"

# get the new menu as txt
configtxt=process.dumpPython()

# check if the new path is in the menu
if not newpathname in configtxt:
    print "Ooops, new path not found in the process..!"
    sys.exit()

# Form a text string from metadata to be written to the new menu as header
chtxt="#"+"\n# ".join(changes)
myname=os.path.basename(sys.argv[0])
meta="""# HLT menu python configuration file, autogenerated by %s at %s
# menu file: %s
# %s (base path) ->- %s (new path)
# cloned/created by applying the following changes:
%s
""" % (myname, str(datetime.now())[:-10], os.path.abspath(hlt_ifile), basepath, newpathname, chtxt)
configtxt=meta+"\n"+configtxt

# Add release specific code as epilogue if asked
if appendepilogue: configtxt=configtxt+"\n"+open("epilogue.txt").read()

#Write-out the new menu
file(hlt_ofile,"w").write(configtxt)
if verbose: print "wrote",hlt_ofile
