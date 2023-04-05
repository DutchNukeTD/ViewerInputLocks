# Python 3
# 2023-04-04
# Golan version of the viewer node
# Works Together with script GB_misc.py

# Add buttons to the 'Viewer1' node. 

import nuke

def viewer():
    try:
        viewerNode = nuke.thisNode()
        # Checks if viewerNode already has the wanted to add knobs. 
        # If so do nothing.

        if viewerNode['name'].value() == 'Viewer1':
            if not viewerNode.knob('Locks'):
                locksTab = nuke.Tab_Knob('Locks')
                viewerNode.addKnob(locksTab)

                locks = [ i for i in range(1,10)]
                locks.append(0) # keyboard '0' needs to be on the 10e place. 
                
                for i in locks:
                    string = 'lock' + str(i)
                    string = nuke.Boolean_Knob(string)
                    string.clearFlag(nuke.STARTLINE)
                    string.setFlag(nuke.STARTLINE)
                    viewerNode.addKnob(string)
                    nodeName = '_nodeName' + str(i)
                    nodeName = nuke.EvalString_Knob(nodeName, '')
                    nodeName.setValue('None')
                    nodeName.setFlag(nuke.DISABLED)
                    nodeName.clearFlag(nuke.STARTLINE)
                    nodeName.setFlag(nuke.ENDLINE)
                    nodeName.setTooltip('viewer input connected to')
                    viewerNode.addKnob(nodeName)
                
                #AlwaysConnect button
                alwaysConnect = nuke.Enumeration_Knob('alwaysConnect', 'Always connect',['On', 'Off'])
                tooltip = """On: Connects to locked node even is selected node is different. 
    Off: Only connected to locked node if selected node is the same. """
                alwaysConnect.setTooltip(tooltip)
                viewerNode.addKnob(alwaysConnect)

                # Connect With Mouse Off and On
                connectWithMouseOn = nuke.PyScript_Knob('connectWithMouseOn', 'Connect with mouse ON')
                tooltip = """ "May slow down your Nuke!"

    On: Locks keep up to date when reconnecting viewer inputs with you mouse.

    Off: Locks don't update when viewer input is switched with mouse. """
                connectWithMouseOn.setTooltip(tooltip)
                viewerNode.addKnob(connectWithMouseOn)
                callback = """ 
    updateInput = '''nodeName = nuke.thisNode().name()
    knobName = nuke.thisKnob().name()
    knobValue = nuke.thisKnob().value()
    viewerNode = nuke.thisNode()
    #print(str(knobName) + str(knobValue))


    if knobName == 'inputChange':
        inputs = viewerNode.inputs()
        viewerInputs = viewerNode.dependencies()
        viewerInputsList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        count = 0
        number = 0

        # Disconnecting the last viewer node input.
        # Set all '_nodeName..' knobs to 'None'
        if len(viewerNode.dependencies()) == 0:

            for input in viewerInputsList:
                knob = '_nodeName' + str(input)
                viewerNode[knob].setValue('None')
        else:
            for input in viewerInputsList:
                input = int(input)
                knob = '_nodeName' + str(input+1)
                if not viewerNode.input(input) == None:
                    nodeName = viewerNode.input(input).name()
                    viewerNode[knob].setValue(nodeName)
                else:
                    try:
                        viewerNode[knob].setValue('None')                        
                    except NameError: #knob _nodeName10+ does not exist
                        pass 
    '''
    # First set the callback
    nuke.thisNode()['knobChanged'].setValue(updateInput)

    # Disable this knob
    nuke.thisKnob().setEnabled(False) # Set MouseOn back OFF
    nuke.thisNode()['connectWithMouseOff'].setEnabled(True) # Set MouseOff back ON
    """
                connectWithMouseOn.setValue(callback)
                connectWithMouseOn.setFlag(nuke.STARTLINE)

                # Create the Off button
                connectWithMouseOff = nuke.PyScript_Knob('connectWithMouseOff', 'Connect with mouse OFF')
                connectWithMouseOff.clearFlag(nuke.STARTLINE)
                connectWithMouseOff.setFlag(nuke.ENDLINE)
                nuke.thisNode().addKnob(connectWithMouseOff)
                connectWithMouseOff.setEnabled(False) 
                #Script for connectWithMouseOff
                connectWithMouseOffValue = '''nuke.thisNode()['knobChanged'].setValue('') # Remove callback
    nuke.thisNode()['connectWithMouseOn'].setEnabled(True) # Set MouseOn back ON
    nuke.thisKnob().setEnabled(False) # Set MouseOff back OFF'''
                nuke.thisNode()['connectWithMouseOff'].setValue(connectWithMouseOffValue)            
                
                # Diverderline + extra tool tip (ctrl+alt+number)
                diverderline = nuke.Text_Knob('')
                viewerNode.addKnob(diverderline)
                extraTipText = """ Extra tooltips:
    1. Open viewer 'Locks' properties with 'alt+v'.  
    2. If input is disconnected and _nodeName value is still visible you can reconnect the input with 'alt+index'.
    3. Set selected node input to _nodeNames node with 'shift+index.'
    4. Open _nodeNames node properties with 'ctrl+alt+index'."""
                extraTip = nuke.Text_Knob('_extraTip','', extraTipText)
                viewerNode.addKnob(extraTip)

        else: 
            #nuke.message("Dit 'viewerNode.knob Locks' is net gevonden!") --> Message wordt getoond
            # Setting the lock knobs flags again. It seems it doens't get saved.
            pass

        # Default settings locks: 
        # viewer locks 
        viewerNode['lock5'].setValue(True)
        viewerNode['lock6'].setValue(True)
        viewerNode['lock7'].setValue(True)
        viewerNode['lock8'].setValue(True)
        viewerNode['alwaysConnect'].setValue(0) # On
        #connectWithMouseOn.execute() # On - Remove the first '#' to set the connectWithMouseOn ON on start. 

    except:
        pass
