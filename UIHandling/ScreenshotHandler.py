from PIL import ImageGrab as imggrab
import os
import time
import cv2


'''
Responsible for saving and returning screenshots. Also responsible for clearing old no longer used screenshots.
Configurable how many screenshots should be kept before the oldest gets deleted.
'''
class ScreenshotHandler():
    SCREENSHOTDIR = "\\\\screenshots"
    SCREENSHOTPREFIX = "\\\\screenshot-"
    FILEENDING = ".png"

    # Takes a screenshot of the entire viewport
    def getScreenshot(self):
        return self._takeAndReturnScreenshot(())



    # Takes a screenshot of the entire viewport and returns it as a openCV2 image
    def getScreenshotCV2(self):
        imgName = self.SCREENSHOTDIR + self.SCREENSHOTPREFIX + str(int(time.time()))
        self._takeAndSaveScreenshot((), imgName)

        cv2Image = cv2.imread(os.getcwd() + imgName + self.FILEENDING)
        return cv2Image

    def getScreenshotWithinBoundingbox(self, box):
        return self._takeAndReturnScreenshot(box)

    # takes a screenshot of the area specified by the boundingbox "box" parameter
    # img.save(os.getcwd() + self.SCREENSHOTDIR + self.SCREENSHOTPREFIX + str(int(time.time())) + FILEENDING, "PNG")
    def _takeAndSaveScreenshot(self, box, name):
        img = imggrab.grab(box)
        img.save(os.getcwd() + name + self.FILEENDING, self.FILEENDING.upper())

    def _takeAndReturnScreenshot(self, box):
        img = imggrab.grab(box)

        return img


