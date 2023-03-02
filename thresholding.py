# Simple thresholding 
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="my-whole.jpg", help="path to input image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)

#  apply basic thresholding -- the first parameter is the image we want to threshold
# the second value is is our threshold check; if a pixel value is greater than our threshold (in this
# case, 200), we set it to be *black, otherwise it is *white*
(T, thresholdBinaryInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", thresholdBinaryInv)

(T1, thresholdInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresholdInv)

masked = cv2.bitwise_and(img, img, mask=thresholdInv)
cv2.imshow("Output", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()