# Cropping the image

import cv2

img = cv2.imread('my-whole.jpg')
print(img.shape) # gives the shape (height, width, rgb) = (384, 576, 3)

imgCropped = img[75:280, 0:576] # we want the face without text

cv2.imshow('Cropped Image',imgCropped)
cv2.waitKey(0)
cv2.destroyAllWindows()