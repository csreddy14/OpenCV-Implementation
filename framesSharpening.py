# Sharpening the frames extracted from a video
import cv2
import numpy as np

# Import the image
img = cv2.imread(r'C:\Users\chant\OneDrive\Desktop\OpenCV\Extracted\frame66.jpg')

# Gaussian kernel for sharpening
gaussian_blur = cv2.GaussianBlur(img, (7,7), 2)

# Sharpening using addWeighted()
sharp1 = cv2.addWeighted(img, 1.5, gaussian_blur, -0.5, 0) # algorithm for addWeighted is src1*aplha + src2*beta + gamma
sharp2 = cv2.addWeighted(img, 3.5, gaussian_blur, -2.5, 0)
sharp3 = cv2.addWeighted(img, 7.5, gaussian_blur, -6.5, 0)

# Show the sharpened images
cv2.imshow("Sharpened 3", sharp3)
cv2.imshow("Sharpened 2", sharp2)
cv2.imshow("Sharpened 1", sharp1)
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()