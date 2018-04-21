'''
Responsible for getting pressed keys

Can place the following code into a method in the main class
Call:
thread.start(listenForUserInput)

Code:
def listenForUserInput(self):
    getch/getwch?
    something else?
'''

class ExternalUserInput():

    def registerListener(self, listener):
        try:
            self.listeners.append(listener)
        except:
            self.listeners = []
            self.listeners.append(listener)




    def mainListeningThread(self):
        # Listen for user input and on input call listeners

    def callListeners(self, event):
        for listener in self.listeners:
            listener.externalUserInputDetected(event)