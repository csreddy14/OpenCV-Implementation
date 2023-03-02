# Applying filters on extracted frames
import cv2
import numpy as np

# Import image
img = cv2.imread(r'C:\Users\chant\OneDrive\Desktop\OpenCV\Extracted\frame66.jpg')
rows, cols = img.shape[:2]

# Kernel blurring using filter2D()
kernel_25 = np.ones((25,25), np.float32) / 625.0
output_kernel = cv2.filter2D(img, -1, kernel_25)

# Boxfliter and blur function blurring
output_blur = cv2.blur(img, (25,25))
output_box = cv2.boxFilter(img, -1, (5,5), normalize=False) # normalise=False increases the intensity of the image, suppose if we have dark image it will increase its intensity and makes it bright

# Gaussian Blur
output_gaus = cv2.GaussianBlur(img, (5,5), 0)

# Median Blur is used for reduction of Noise in an image
output_med = cv2.medianBlur(img, 5)

# Bilateral is used for reduction of noise and preserving of edges of image
output_bil = cv2.bilateralFilter(img, 5, 6, 6)


cv2.imshow("Kernel Blur", output_kernel)
cv2.imshow("Blur() output", output_blur)
cv2.imshow("Box filter", output_box)
cv2.imshow("Gaussian Blur", output_gaus)
cv2.imshow("Median Blur", output_med)
cv2.imshow("Bilateral", output_kernel)
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()