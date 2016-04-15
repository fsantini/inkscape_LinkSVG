# Inkscape LinkSVG
Inkscape extension to link an element from an external SVG file

This extension allows you to insert an element from an external SVG file and update it when the external file is updated.

## Installation ##

Copy the `*.py` and the `*.inx`files into your Inkscape extension directory.
Under Linux it would be something like:

    /usr/share/inkscape/extensions
or (locally):

    ~/.config/inkscapte/extensions

## Usage ##

The extension will add a `Link SVG` submenu in your `Extensions` menu in Inkscape. Under this submenu, two entries exist. `Insert SVG...` will allow you to import an element from an external SVG file. Write the full path (absolute!) in the `Input File` field and the ID of the element to add in the `SVG ID` field.
The Id can be identified in inkscape by right-clicking on an object and selecting `Object Properties`.

The source file will now be linked. If it is modified, you will need to use the `Update SVG Links` menu entry to reflect the changes in your document.

## Caveats ##
Only absolute paths are allowed to define the source file, so moving a source file will break the connection. The path can be updated using the XML Editor of Inkscape.


> Written with [StackEdit](https://stackedit.io/).