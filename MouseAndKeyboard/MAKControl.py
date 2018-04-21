import abc
import time
'''
This class defines behavior for interacting with the mouse and keyboard programatically.
An os specific version is required to be implemented

@author: Mattis Andersson
'''

class MAKControl():
    __metaclass__ = abc.ABCMeta

    ###########################################################################
    ## Mouse movement section
    ###########################################################################

    @abc.abstractmethod
    def moveMouseToPosition(self, xCord, yCord):
        raise NotImplementedError("User must implement moveMouseToPosition")

    ###########################################################################
    ## Scrolling section
    ###########################################################################
    @abc.abstractmethod
    def mouseScrollPos(self, scrollAmount, xCord, yCord):
        raise NotImplementedError("User must implement mouseScrollPos")

    def mouseScroll(self, scrollAmount):
        self.mouseScrollPos(scrollAmount, 0, 0)

    ###########################################################################
    ## Mouse clicking section
    ###########################################################################

    # mode defines which mode the given coordinate is "evented" in, it could for example be left down etc.
    @abc.abstractmethod
    def mouseEvent(self, xCord, yCord, mode):
        raise NotImplementedError("User must implement mouseEvent")

    # Moves the mouse to the given coordinates before the given action by "mode" is done
    def moveMouseToCoordAndDoAction(self, xCord, yCord, mode):
        self.moveMouseToPosition(xCord, yCord)
        self.mouseEvent(0, 0, mode)

    ###########################################################################
    ## Keyboard interaction section
    ###########################################################################
    @abc.abstractmethod
    def keysDown(self, *keys):
        raise NotImplementedError("User must implement keysDown")

    @abc.abstractmethod
    def keysUp(self, *keys):
        raise NotImplementedError("User must implement keysUp")

    def pressKeys(self, holdDownFor=0.05, *keys):
        self.keysDown(keys)
        time.sleep(holdDownFor)
        self.keysUp(keys)
