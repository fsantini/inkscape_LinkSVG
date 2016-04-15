#!/usr/bin/env python

# insertSVG.py
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

def log(logstr):
  with open('/home/francesco/inktest/test.log', 'a') as l:
    l.write(logstr)
    l.write('\n')

class InsertSVG(inkex.Effect):
    """
    Example Inkscape effect extension.
    Creates a new layer with a "Hello World!" text centered in the middle of the document.
    """
    def __init__(self):
        """
        Constructor.
        Defines the "--what" option of a script.
        """
        # Call the base class constructor.
        inkex.Effect.__init__(self)

        # Define string option "--what" with "-w" shortcut and default value "World".
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
                 
        inputTree = inkex.etree.parse(self.options.file)
        # get the elemement with the desired ID
        desiredElement = None
        for elem in inputTree.getroot().iter():
          if elem.get('id') == self.options.importId:
            desiredElement = elem
            break
          
        if desiredElement is None:
          return
        
        # Get access to main SVG document element and get its dimensions.
        svg = self.document.getroot()


        # Create a new layer.
        layer = inkex.etree.SubElement(svg, 'g')
        layer.set(inkex.addNS('label', 'inkscape'), 'InsertedFileGroup')
        layer.set('filepath', self.options.file)
        layer.set('import_id', self.options.importId)
        
        # Connect elements together.
        layer.append(desiredElement)

# Create effect instance and apply it.
effect = InsertSVG()
effect.affect()