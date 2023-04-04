import nuke

# Viewer Lock opties
import GB_Viewer 
nuke.addOnCreate(GB_Viewer.viewer, nodeClass='Viewer')

# Viewer menu + shortcut
def openViewerPanelLock():
    nuke.toNode('Viewer1').showControlPanel()
    nuke.toNode('Viewer1').setTab(3)
nuke.menu('Nuke').addCommand('Viewer/viewer locks', 'openViewerPanelLock()', 'alt+v')

# Import misc_Golan # Copy from original. 
import GB_misc
nukescripts.connect_selected_to_viewer = GB_misc.connect_selected_to_viewer
menubar = nuke.menu("Nuke")
m = menubar.addMenu("Viewer")
n = m.addMenu("Connect to saved nodes")
# set selected node input to saved _nodeName
n.addCommand("Using Input 1", "GB_misc.inputViewerNodeName(0)", "shift+1", shortcutContext=dagContext)
n.addCommand("Using Input 2", "GB_misc.inputViewerNodeName(1)", "shift+2", shortcutContext=dagContext)
n.addCommand("Using Input 3", "GB_misc.inputViewerNodeName(2)", "shift+3", shortcutContext=dagContext)
n.addCommand("Using Input 4", "GB_misc.inputViewerNodeName(3)", "shift+4", shortcutContext=dagContext)
n.addCommand("Using Input 5", "GB_misc.inputViewerNodeName(4)", "shift+5", shortcutContext=dagContext)
n.addCommand("Using Input 6", "GB_misc.inputViewerNodeName(5)", "shift+6", shortcutContext=dagContext)
n.addCommand("Using Input 7", "GB_misc.inputViewerNodeName(6)", "shift+7", shortcutContext=dagContext)
n.addCommand("Using Input 8", "GB_misc.inputViewerNodeName(7)", "shift+8", shortcutContext=dagContext)
n.addCommand("Using Input 9", "GB_misc.inputViewerNodeName(8)", "shift+9", shortcutContext=dagContext)
n.addCommand("Using Input 10", "GB_misc.inputViewerNodeName(9)", "shift+0", shortcutContext=dagContext)

# Still connect to viewer even is lock(index) in enabled!
n.addCommand("alwasy connect 1", "GB_misc.alwaysConnectToViewer(0)", "alt+1", shortcutContext=dagContext)
n.addCommand("alwasy connect 2", "GB_misc.alwaysConnectToViewer(1)", "alt+2", shortcutContext=dagContext)
n.addCommand("alwasy connect 3", "GB_misc.alwaysConnectToViewer(2)", "alt+3", shortcutContext=dagContext)
n.addCommand("alwasy connect 4", "GB_misc.alwaysConnectToViewer(3)", "alt+4", shortcutContext=dagContext)
n.addCommand("alwasy connect 5", "GB_misc.alwaysConnectToViewer(4)", "alt+5", shortcutContext=dagContext)
n.addCommand("alwasy connect 6", "GB_misc.alwaysConnectToViewer(5)", "alt+6", shortcutContext=dagContext)
n.addCommand("alwasy connect 7", "GB_misc.alwaysConnectToViewer(6)", "alt+7", shortcutContext=dagContext)
n.addCommand("alwasy connect 8", "GB_misc.alwaysConnectToViewer(7)", "alt+8", shortcutContext=dagContext)
n.addCommand("alwasy connect 9", "GB_misc.alwaysConnectToViewer(8)", "alt+9", shortcutContext=dagContext)
n.addCommand("alwasy connect 10", "GB_misc.alwaysConnectToViewer(9)", "alt+0", shortcutContext=dagContext)

# Open node properties from _nodeName(index)
n.addCommand("properties Input 1", "GB_misc.openProperties(0)", "ctrl+alt+1", shortcutContext=dagContext)
n.addCommand("properties Input 2", "GB_misc.openProperties(1)", "ctrl+alt+2", shortcutContext=dagContext)
n.addCommand("properties Input 3", "GB_misc.openProperties(2)", "ctrl+alt+3", shortcutContext=dagContext)
n.addCommand("properties Input 4", "GB_misc.openProperties(3)", "ctrl+alt+4", shortcutContext=dagContext)
n.addCommand("properties Input 5", "GB_misc.openProperties(4)", "ctrl+alt+5", shortcutContext=dagContext)
n.addCommand("properties Input 6", "GB_misc.openProperties(5)", "ctrl+alt+6", shortcutContext=dagContext)
n.addCommand("properties Input 7", "GB_misc.openProperties(6)", "ctrl+alt+7", shortcutContext=dagContext)
n.addCommand("properties Input 8", "GB_misc.openProperties(7)", "ctrl+alt+8", shortcutContext=dagContext)
n.addCommand("properties Input 9", "GB_misc.openProperties(8)", "ctrl+alt+9", shortcutContext=dagContext)
n.addCommand("properties Input 10", "GB_misc.openProperties(9)", "ctrl+alt+0", shortcutContext=dagContext)