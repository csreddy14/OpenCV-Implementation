# Edge Detection for extracted frames of a video
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default=r"C:\Users\chant\OneDrive\Desktop\OpenCV\Extracted\frame66.jpg", help="path to input image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)

edged = cv2.Canny(blurred,10,100)

cv2.imshow("Edged Image", edged)

cv2.waitKey(0)
cv2.destroyAllWindows