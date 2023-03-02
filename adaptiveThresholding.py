# Otsu thresholding 
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="my-whole.jpg", help="path to input image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)

# apply adaptive thresholding
ret,th1 = cv2.threshold(blurred,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
cv2.imshow("Simple Threshold", th1)
cv2.imshow("Adaptive Threshold Mean C", th1)
cv2.imshow("Adaptive Threshold Gaussian C", th1)
# visualize only the masked regions in the image
masked = cv2.bitwise_and(img, img, mask=th1)
cv2.imshow("Output", masked)
cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()