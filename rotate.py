# Rotating the image

import cv2

img = cv2.imread('my-whole.jpg')
cv2.imshow('Original Image',img)

imgRotated90Clock = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) #rotate image by 90degrees clockwise.
imgRotated90AntiClock = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) #rotate image by 90degrees anti clockwise.
imgRotated180 = cv2.rotate(img, cv2.ROTATE_180) #rotate image by 180degrees.


cv2.imshow('Rotated 90degrees Clockwise',imgRotated90Clock)
cv2.imshow('Rotated 90degrees Anti Clockwise',imgRotated90AntiClock)
cv2.imshow('Rotated 180degrees',imgRotated180)
cv2.waitKey(0)
cv2.destroyAllWindows()