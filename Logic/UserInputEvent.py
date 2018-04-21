'''
Hold information about external user input, such as for example which key was pressed etc.
'''

class UserInputEvent():

    def __init__(self, pressedKeys):
        self.pressedKeys = pressedKeys

    def getPressedKeys(self):
        return self.pressedKeys