# Copyright (c) 2009 The Foundry Visionmongers Ltd.  All Rights Reserved.

import nuke_internal as nuke
import nukescripts
import random
import os
import textwrap

###############################################################################
def indexInfo(index):
    # info inputIndex 
  if index == 9:
    lockNumber = 'lock0'
    nodeName = '_nodeName0'
  else:
    lockNumber = 'lock' + str(index+1)
    nodeName = '_nodeName' + str(index+1)

  return lockNumber, nodeName
###############################################################################


def connect_selected_to_viewer(inputIndex):
  """Connects the selected node to the given viewer input index, ignoring errors if no node is selected."""
  selection = None
  try:
    selection = nuke.selectedNode()
  except ValueError:  # no node selected
    pass

  if selection is not None and selection.Class() == 'Viewer':
    selection = None

  ###############################################
  ############### added by Golan ################
  ###############################################
  viewerNode = nuke.toNode('Viewer1')
  
  # info inputIndex 
  lockNumber, nodeName = indexInfo(inputIndex)

  # locked
  viewer = nuke.activeViewer()

  # Check if 'nuke.connectViewer' connects with 'viewer1' by checking which viewer windows is active. 
  if viewer.node()['name'].value() == 'Viewer1':

    try:

      if viewerNode[lockNumber].value() == True:
          # No selected node --> Go to connected node

          if selection == None:

            selection = nuke.toNode(viewerNode[nodeName].value())
            nuke.connectViewer(inputIndex, selection)
    
          # Selected node == locked Node
          elif viewerNode[nodeName].value() == selection.name():
            nuke.connectViewer(inputIndex, selection)
    
          # Locked node is empty
          elif viewerNode[nodeName].value() == 'None':
            nuke.connectViewer(inputIndex, selection)

            try:
              viewerNode[nodeName].setValue(selection.name())

            except:
              pass
    
          # Selected node != locked node
          else:

            if viewerNode['alwaysConnect'].getValue() == 0: # Always connect = ON

              lockedNode = nuke.toNode(viewerNode[nodeName].value())
              nuke.connectViewer(inputIndex, lockedNode)
            else: # Always connect = OFF
              pass # do not connect.
        # unlocked
      else: 
        nuke.connectViewer(inputIndex, selection)

        try:
          viewerNode[nodeName].setValue(selection.name())

        except:
          pass

    except NameError: #Probably viewer input node above 0 
      pass

  else: 
    nuke.connectViewer(inputIndex, selection)



def alwaysConnectToViewer(index):
  """Connects the selected node to the given viewer input index, even if 'lock' is enabled."""
  selection = None
  try:
    selection = nuke.selectedNode()
  except ValueError:  # no node selected
    pass

  if selection is not None and selection.Class() == 'Viewer':
    selection = None

  # info inputIndex 
  lockNumber, nodeName = indexInfo(index)

  # Viewer node
  viewerNode = nuke.toNode('Viewer1')

  # Check if 'nuke.connectViewer' connects with 'viewer1' by checking which viewer windows is active. 
  viewer = nuke.activeViewer()
  if viewer.node()['name'].value() == 'Viewer1':
  
    if selection is not None:
      # Connect node to viewer
      nuke.connectViewer(index, selection)

      try:
        viewerNode[nodeName].setValue(selection.name())

      except:
        pass

    # selection is none
    # but _nodeName has a value
    else: 
      if viewerNode[nodeName].value() != 'None':

        try:
          nodeName = viewerNode[nodeName].value()
          selection = nuke.toNode(nodeName)
          nuke.connectViewer(index, selection)
          
        except:
          pass



def inputViewerNodeName(index):
  """Connects the selected node to the given viewer input index, ignoring errors if no node is selected."""
  selection = None
  try:
    selection = nuke.selectedNode()
  except ValueError:  # no node selected
    pass

  if selection is not None and selection.Class() == 'Viewer':
    selection = None

  # info inputIndex 
  lockNumber, nodeName = indexInfo(index)

  # Viewer node
  viewerNode = nuke.toNode('Viewer1')

  # Check if 'nuke.connectViewer' connects with 'viewer1' by checking which viewer windows is active. 
  viewer = nuke.activeViewer()
  if viewer.node()['name'].value() == 'Viewer1':

    # There is no node selected.
    # RECONNECT viewer node with saved _nodeName(index).
    if selection == None:
      selection = nuke.toNode(viewerNode[nodeName].value())
      nuke.connectViewer(index, selection)

    # With a node selected other than the viewer node.
    # CONNECT selected node with saved _nodeName(index).
    else:
      # set selected node and second node (that's in de viewer _nodeName saved) as selected.
      nodeName = viewerNode[nodeName].value()
      nodeName = nuke.toNode(nodeName)
      nodeName.setSelected(True)

      # connect the nodes
      nuke.connectNodes(False, False)

      # deselect nodeName
      # If not deselected and connect to another node again, it can bug the script, because more than 2 nodes are selected. 
      nodeName.setSelected(False)



def openProperties(index):
  """Functions creates a shortcut for a quick properties opening for the saved viewer nodes _nodeNames. shift+index """
    # info inputIndex 
  lockNumber, nodeName = indexInfo(index)

  # get index _nodeName value
  # go to Node and open properties
  viewerNode = nuke.toNode('Viewer1')
  indexNode = viewerNode[nodeName].value()
  indexNode = nuke.toNode(indexNode)
  indexNode.showControlPanel()
  

