'''
Concrete implementation of the abstract class MAKControl

@author: Mattis Andersson
'''

import win32api

import win32con

import MAKControl
import VKKeysLookup


class MAKControlWindows(MAKControl):
    modeTable = {"LEFTDOWN" : win32con.MOUSEEVENTF_LEFTDOWN,
                              "LEFTUP" : win32con.MOUSEEVENTF_LEFTUP}

    ###########################################################################
    ## Mouse movement section
    ###########################################################################
    def moveMouseToPosition(self, xCord, yCord):
        win32api.SetCursorPos((xCord, yCord))

    ###########################################################################
    ## Scrolling section
    ###########################################################################
    def mouseScrollPos(self, scrollAmount, xCord, yCord):
        # Each wheel click == 120...
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, xCord, yCord, scrollAmount * 120)

    ###########################################################################
    ## Mouse clicking section
    ###########################################################################
    # mode defines which mode the given coordinate is "evented" in, it could for example be left down etc.
    def mouseEvent(self, xCord, yCord, mode):
        win32api.mouse_event(modeTable[mode], xCord, yCord)

    ###########################################################################
    ## Keyboard interaction section
    ###########################################################################
    
    def keysDown(self, *keys):
        for key in keys:
            win32api.keybd_event(VKKeysLookup.lookupKey(key), 0, 0, 0)
        raise NotImplementedError("User must implement keysDown")

    
    def keysUp(self, *keys):
        for key in keys:
            win32api.keybd_event(VKKeysLookup.lookupKey(key), 0, win32con.KEYEVENTF_KEYUP, 0)