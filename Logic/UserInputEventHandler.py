import abc
''''
Responsible for handling the events of external user input.
Should be overriden by a concrete class with the application unique logic.
'''

class UserInputEventHandler():

    __metaclass__ = abc.ABCMeta


    @abc.abstractmethod
    def externalUserInputDetected(self, event):
        raise NotImplementedError("User must implement logic for external user input")