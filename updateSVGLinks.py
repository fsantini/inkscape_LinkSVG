#!/usr/bin/env python

# updateSVGLinks.py
# Copyright 2016 Francesco Santini <francesco.santini@gmail.com>
# Licensed under a MIT license. See LICENSE for details.

# These two lines are only needed if you don't put the script directly into
# the installation directory
import sys
sys.path.append('/usr/share/inkscape/extensions')

# We will use the inkex module with the predefined Effect base class.
import inkex
# The simplestyle module provides functions for style parsing.
from simplestyle import *
import os

def getElementFromFile(fname, elemID):
  inputTree = inkex.etree.parse(fname)
  desiredElement = None
  for elem in inputTree.getroot().iter():
    if elem.get('id') == elemID:
      desiredElement = elem
      break
    
  return desiredElement

class UpdateSVG(inkex.Effect):
    """
    Example Inkscape effect extension.
    Creates a new layer with a "Hello World!" text centered in the middle of the document.
    """
    def __init__(self):
        """
        Constructor.
        """
        # Call the base class constructor.
        inkex.Effect.__init__(self)

        self.OptionParser.add_option('-f', '--file', action = 'store',
          type = 'string', dest = 'file',
          help = 'Source svg file')
        
        self.OptionParser.add_option('-i', '--importid', action = 'store',
          type = 'string', dest = 'importId',
          help = 'Element ID to be added')
        

    def effect(self):
        """
        Effect behaviour.
        Overrides base class' method and inserts "Hello World" text into SVG document.
        """
        # Get access to main SVG document element and get its dimensions.
        svg = self.document.getroot()
    
        for elem in svg:
          if elem.get(inkex.addNS('label', 'inkscape')) == 'InsertedFileGroup':
            fname = elem.get('filepath')
            importId = elem.get('import_id')
            # clear the children of this element
            for child in elem:
              elem.remove(child)
            
            elem.append(getElementFromFile(fname, importId))

# Create effect instance and apply it.
effect = UpdateSVG()
effect.affect()