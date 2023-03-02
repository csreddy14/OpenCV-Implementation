# Color spaces of the image
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="my-whole.jpg", help="path to input image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])

# convert RGB to HSV and print H, S and V separately
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow('HSV',hsv)

# for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
#     cv2.imshow(name, chan)

# convert RGB to L*a*b and print L*, a* and b* separately
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('L*a*b*',lab)

for (name, chan) in zip(("L*", "a*", "b*"), cv2.split(lab)):
    cv2.imshow(name, chan)

cv2.waitKey(0)
cv2.destroyAllWindows()