# Contour Detection 
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="objects.jpg", help="path to input image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)

edged = cv2.Canny(blurred,10,100)

contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
copyImg = img.copy()

cv2.drawContours(copyImg, contours, -1, (0,255,0), 2)
print(len(contours), "objects were found in this image.")

cv2.imshow("Edged Image", edged)
cv2.imshow("Contours", copyImg)

cv2.waitKey(0)
cv2.destroyAllWindows