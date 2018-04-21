import abc
import thread
import time

'''
"Main" framework component, responsible for getting the objects on screen and deciding what to do...
Should be overridden with a concrete implementation...

Or maybe this should just call "userLogic" which will be a class with a method accepting the uiHandlers detected
objects and the mouseAndKeyboardControl and which will decide what to do on the received input


No... Now what a user needs to do is to implement the detectUserInputThread method
'''
class InteractionsController():

    __metaclass__ = abc.ABCMeta

    def __init__(self, mouseAndKeyboardControl, uiHandler, userLogic):
        self.mouseAndKeyboardControl = mouseAndKeyboardControl
        self.uiHandler = uiHandler

    # Main entry point of the program, this will be the "game-loop" class, responsible for
    # calling all the responsible classes and "transmitting" this information to the
    # user specified methods which will decide what to do on the information received...
    def main(self):
        self.exitMainLoop = False
        self.exitSubThread = False

        thread.start_new_thread(self.detectUserInputThread, ())

        while(not(self.exitMainLoop)):
            pass

        self.exitSubThread = True


    def detectUserInputThread(self):
        while(not(self.exitSubThread)):
            self.userInput() # recieve user input

    # This method will register user input and decide what to do with it, it could for example if it detected
    # a space-key press exit the program by setting the exitMainLoop to True...
    @abc.abstractmethod
    def userInput(self):
        raise NotImplementedError("User must implement moveMouseToPosition")

    @abc.abstractmethod
    def actUponFeedback(self, foundObjectAndTheirLocations):
        raise NotImplementedError("User must implement moveMouseToPosition")
