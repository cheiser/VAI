'''
Responsible for detecting objects on screen and for triggering events when new objects are detected.

@author: Mattis Andersson
'''


def UIHandler():
    detectObjects = [] # Will hold the objects that are detectable, each object can then hold coordinates they are
    # allowed to be detected within or None/empty if they are detectable anywhere on screen. It will be
    # possible to specify exact coordinates to simplify detection of the objects... UIObject...
    

