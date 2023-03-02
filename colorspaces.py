# Color spaces of the image
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="my-whole.jpg", help="path to input image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
cv2.imshow('RGB',img)

# gives output of red, green and blue percentages separately
for (name, chan) in zip(("B", "G", "R"), cv2.split(img)):
    cv2.imshow(name, chan)

cv2.waitKey(0)
cv2.destroyAllWindows()