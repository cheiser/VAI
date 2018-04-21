'''
Holds data regarding the recieved user input regardless of what concrete implementation is used to detect the event
'''

class UserInputKeyboardEvent():
    def __init__(self, keyName, isExtended, isInjected, isAlt, isTransition):
        self.keyName = keyName
        self.isExtended = isExtended
        self.isInjected = isInjected
        self.isAlt = isAlt
        self.isTransition = isTransition

    def getKeyName(self):
        return self.keyName

    def IsExtended(self):
        return self.isExtended

    def IsInjected(self):
        return self.isInjected

    def IsAlt(self):
        return self.isAlt

    def IsTransition(self):
        return self.isTransition