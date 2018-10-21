import cv2
import numpy as np

# THIS FILE WAS MERELY FOR TESTING AND IS ONLY KEPT FOR SENTIMENTAL REASONS...

# Finds the coordinates of the sub image inside the super image and returns them as a tuple
# (-1, -1) is returned if no match is found
def findCoordinatesOfImage(super, sub):
    (x, y) = findBestMatchCoordinates(super, sub) # TODO: FINISH THIS!!!

    matchScore = calculateMatchScore(super, sub, (x, y))

    print "matchscore:"
    print matchScore

    print "sub.size:"
    print sub.size

    if(matchScore < 0.5):
        return (x, y)
    else:
        return (-1, -1)

# Returns the coordinates in the super image best matched by the sub image
# should return a tuple with the x and y coordinate of the match...
def findBestMatchCoordinates(super, sub):
    result = cv2.matchTemplate(super, sub, cv2.TM_CCOEFF_NORMED)

    return np.unravel_index(result.argmax(), result.shape)

# Simply subtracts the sub from the super at the start position to the size of the sub
# and calculates the absolute sum
# The smaller the better, 0 == almost perfect match
def calculateMatchScore(super, sub, (x, y)):
    superCropped = super[x:x+sub.shape[0], y:y+sub.shape[1], :]


    normalized = abs(superCropped - sub) / 255.0
    normalized = np.ceil(normalized)

    return normalized.sum()

# Main testing method. Should be removed at a later time...
def main():
    # load super image
    superImg = cv2.imread("screenshots/super.PNG")

    # load sub image
    # subImg = cv2.imread("screenshots/almostmatch - kopia.PNG")
    subImg = cv2.imread("screenshots/sub.PNG")

    # find coordinates of sub image
    (x, y) = findCoordinatesOfImage(superImg, subImg)

    print "found coordinates: "
    print x
    print y

    print "super shape: "
    print superImg.shape

    print "sub shape: "
    print subImg.shape

    subImageOfResult = superImg[x:x+subImg.shape[0], y:y+subImg.shape[1],:]

    # subImageOfResult = superImg[0:200, 0:200]

    print "subimage result"
    print subImageOfResult.shape

    cv2.imshow("test", subImageOfResult)
    cv2.waitKey(0)

    # load image which should not match
    nomatchImg = cv2.imread("screenshots/nomatch.PNG")

    # find coordinates of nonmatching image (this should return (-1, -1) when everything is working...
    (x, y) = findCoordinatesOfImage(superImg, nomatchImg)


    print "found coordinates: "
    print x
    print y

    if(x != -1 and y != -1):
        subImageOfResult = superImg[x:x+nomatchImg.shape[0], y:y+nomatchImg.shape[1],:]

        cv2.imshow("test", subImageOfResult)
        cv2.waitKey(0)


if __name__ == '__main__':
    main()