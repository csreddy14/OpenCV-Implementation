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

# apply Otsu's automatic thresholding which automatically determines
# the best threshold value
(T, thresholdBinaryInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold", thresholdBinaryInv)
print("[INFO] otsu's thresholding value: {}".format(T))

# visualize only the masked regions in the image
masked = cv2.bitwise_and(img, img, mask=thresholdBinaryInv)
cv2.imshow("Output", masked)
cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()