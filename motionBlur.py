# Motion Blur for images
import cv2
import numpy as np

img = cv2.imread('my-whole.jpg')
size = 15

kernel = np.zeros((size,size)) # our kernel shape is 15*15
kernel[int((size-1)/2),:] = np.ones(size) # replacing middle row with ones
kernel = kernel/size

output = cv2.filter2D(img, -1, kernel) # Motion blur is used for video processing mainly
cv2.imshow("Motion blurred", output)
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()