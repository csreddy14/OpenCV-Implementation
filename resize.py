# Resizing the image

import cv2

img = cv2.imread('my-whole.jpg')
print(img.shape) # gives the shape (height, width, rgb) = (384, 576, 3)

# resizing the image to (350, 350)
width, height = 350,350
imgResize = cv2.resize(img, (width,height))

print(imgResize.shape)
cv2.imshow('Original',img)
cv2.imshow('Resized',imgResize)
cv2.waitKey(0)
cv2.destroyAllWindows()