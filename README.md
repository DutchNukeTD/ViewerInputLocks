# ViewerInputLocks
## By Golan van der Bend
04-04-2023
Python 3
For Nuke 13.0+
Works Together with script GB_misc.py

## info

****** __Only works when viewer node is called 'Viewer1' without ''__ ******

Adds checkboxes to the 'Viewer1' node properties with the connected node names next to it. 
With a checkbox 'checked' (locked) you disable the viewer node to change that index input node with another.

![Viewer_locks](https://user-images.githubusercontent.com/105785047/230105745-053da5a1-651b-4c54-a641-1ffa0a6876f6.jpg)


*Extra*
With the nodes connected to the 'Viewer1' node you can now:
-Set these nodes as input to a selected node (shift+index).
-Open there properties without first selecting them (ctrl+alt+index).

## Tips:
-You can quick open your viewer lock poperties with 'alt+v'.
-You can find the viewer lock poperties shortcut in de nuke top bar 'viewer - viewer locks'.
-Can you reconnect a locked input with 'alt+index'. 

## Default settings: 
I set the default settings for the locks on 5,6,7 and 8. Those are mine offline, plate, write and render nodes. However you can change that to your liking in the
GB_Viewer file. 

## Install steps: 
1. Add the files 'GB_misc.py' & 'GB_Viewer.py' to the '.nuke' folder location on your computer. If you don't know where that is see: https://support.foundry.com/hc/en-us/articles/207271649-Q100048-Nuke-Directory-Locations.
2. If you don't have a 'menu.py' at the '.nuke' folder location drop this one in there. Otherwise copy everything except the 'import nuke' and paste it in your menu.py file. 

