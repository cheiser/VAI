'''
Represents a single type of object on the screen.
Holds the "image" object and an array of bounding boxes which specifies within which areas of the entire
viewport the object can be detected within.

Also holds a separate array of exact coordinates where the object may be detected. This is to improve performance
by not searching for the location of the object when we already know its location and also to minimize the risk
of accidentially detecting "the object" in a location where it does not exist.

@author: Mattis Andersson
'''

def UIObject():

    # object == the subimage to be detected
    #
    # allowedDetectionAreasBBoxesList == list of bounding boxes within which this specific object is allowed to
    #   be detected
    #
    # specificDetectCoords == Exact coordinates in which we expect this object to appear
    #
    # active == specifies whether or not we should currently detect this object. This is could be used to be able to
    #   create functionality where we can only detect a certain object if another object has first been detected
    #   for example.
    def __init__(self, object, allowedDetectionAreasBBoxesList = [], specificDetectCoords = [], active=True):
        self.object = object
        self.allowedDetectionAreasBBoxesList = allowedDetectionAreasBBoxesList
        self.specificDetectCoords = specificDetectCoords
        self.active = active

    def getUIObject(self):
        return self.object


    def getAllowedDetectionAreas(self):
        return self.allowedDetectionAreasBBoxesList
    
    def getSpecificDetectCoords(self):
        return self.specificDetectCoords

    def isActive(self):
        return self.active

    def setUIObject(self, object):
        self.object = object

    def setAllowedDetectionAreas(self, allowedDetectionAreasBBoxesList):
        self.allowedDetectionAreasBBoxesList = allowedDetectionAreasBBoxesList

    def setSpecificDetectCoords(self, specificDetectCoords):
        self.specificDetectCoords = specificDetectCoords

    # Sets if this object should be active or not...
    def setActiveState(self, active):
        self.active = active