import cv2
import numpy as np

'''
Class for handling object detection inside images

@author: Mattis Andersson
'''
class ObjectInImageDetector():

    CONST_MATCH_SCORE_MATCH = 0.5

    # Finds the coordinates of the sub image inside the super image and returns them as a tuple
    # (-1, -1) is returned if no match is found
    def findCoordinatesOfImage(self, super, sub):
        (x, y) = self.findBestMatchCoordinates(super, sub)

        matchScore = self.calculateMatchScore(super, sub, (x, y))

        if(matchScore < self.CONST_MATCH_SCORE_MATCH):
            return (x, y)
        else:
            return (-1, -1)

    # Returns the coordinates in the super image best matched by the sub image
    # should return a tuple with the x and y coordinate of the match...
    def findBestMatchCoordinates(self, super, sub):
        result = cv2.matchTemplate(super, sub, cv2.TM_CCOEFF_NORMED)

        return np.unravel_index(result.argmax(), result.shape)

    # Simply subtracts the sub from the super at the start position to the size of the sub
    # and calculates the absolute sum
    # The smaller the better, 0 == almost perfect match
    def calculateMatchScore(self, super, sub, (x, y)):
        superCropped = super[x:x+sub.shape[0], y:y+sub.shape[1], :]


        normalized = abs(superCropped - sub) / 255.0
        normalized = np.ceil(normalized)

        return normalized.sum()
