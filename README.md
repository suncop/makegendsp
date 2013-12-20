makegendsp
==========

This python script makes it easier to use external text editors with Cycling 74's GenExpr language, by converting .genexpr text files into .gendsp patch files which can be opened by Max/MSP directly.

Instructions
------------

The script (makegendsp.py) can be run from the command line, and expects a filename of a .genexpr file as it's first argument. It will create a new .gendsp file with the same name in the same directory. Move the .gendsp to somewhere in Max's filepath if it isn't there already, and spawn a new gen~ object with the filename as it's first argument. Voila! If you open the gen~ patcher by double clicking it, you will see that there is a codebox with your code, connected to the correct number of inlets and outlets. If you change your code in the external editor, run the script again and Max's filewatching capabilities will automatically update the file to the new version.

There is also a simple build file for use with Sublime Text, which will allow you to build the .gendsp file by simply hitting the build keystroke. To use it, move the executable makegendsp file to somewhere in your $PATH (/usr/local/bin, for instance), then save gendsp.sublime-build to the Sublime packages folder (should be ~/Library/Application Support/Sublime Text 2/Packages/User on OS X). Restart Sublime Text, and then select gendsp from the Tools>Build System menu. The Sublime Text build script currently does not work on Windows (I think). 