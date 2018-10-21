import unittest
import cv2
import numpy as np
from UIHandling import ObjectInImageDetector

'''
Unit tests which checks so the automatic image detection works...
'''
class ObjectInImageDetectorTest(unittest.TestCase):
    def setUp(self):
        # Read the test file
        self.testImage = cv2.imread("./TestResources/findSubimage.png")
        self.unrelatedImage = cv2.imread("./TestResources/unrelated.png")
        self.imageDetector = ObjectInImageDetector.ObjectInImageDetector()

    def tearDown(self):
        pass

    def testFindSimpleSubsetOfImage(self):
        # Take the test file and get a subportion of it and then input that into the detector class and then get the resulting coordinates and crop the image and make sure they match
        subImage = self.testImage[50:100, 50:100, :]


        (xCord, yCord) = self.imageDetector.findCoordinatesOfImage(self.testImage, subImage)

        self.assertNotEqual(-1, xCord, "Could not find xCord of subimage in superimage")
        self.assertNotEqual(-1, yCord, "Could not find yCord of subimage in superimage")

        self.assertEqual(50, xCord, "Found incorrect index for xCord")
        self.assertEqual(50, yCord, "Found incorrect index for xCord")

        resultSubImage = self.testImage[xCord:xCord+len(subImage), yCord:yCord+len(subImage[0]), :]


        # cv2.imshow("test", resultSubImage)
        # cv2.waitKey(0)

        self.assertEqual(True, self._checkImagesForEquals(subImage, resultSubImage), "The resulting subimage does not match expected")

        # cv2.imshow("test", subImage)
        # cv2.waitKey(0)

        (xCord, yCord) = self.imageDetector.findCoordinatesOfImage(self.testImage, self.unrelatedImage)
        self.assertEqual(-1, xCord, "Found sub image which does not exist")
        self.assertEqual(-1, yCord, "Found sub image which does not exist")


    def _checkImagesForEquals(self, image1, image2):
        if(image1.shape == image2.shape):
            difference = cv2.subtract(image1, image2)
            b, g, r = cv2.split(difference)

            if(cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
                return True

        return False



if __name__ == "__main__":
    unittest.main()