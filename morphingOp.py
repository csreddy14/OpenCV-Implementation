# Morphology operations
import cv2
import numpy as np

img = cv2.imread('my-whole.jpg')

kernel = np.ones((5,5), np.uint8)
# we can use this also
# cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

# Erosion (A pixel in the original image(either 255 or 0) will be considered 255 only if all the pixels under the kernel is 255, otherwise it is eroded(made to zero))
erosion = cv2.erode(img, kernel, iterations=1)

# Dilation (Just opposite to erosion Here, a pixel element is 255 if atleast one pixel under the kernel is 255)
dilation = cv2.dilate(img, kernel, iterations=1)

# Opening (Erosion followed by Dilation) (used in Noise Removal)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Closing (Reverse of Opening(Dilation followed by erosion)) (Filling patches in the foreground object mask)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Gradient (Dilated image - Eroded image) (Used to find outlines of objects)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Top hat (= input image minus Opening image) (Highlights minor details in image(only))
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Black hat (= Closing image minus input image) (To find bright objects on dark background)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
cv2.imshow("Gradient", gradient)
cv2.imshow("Top Hat", tophat)
cv2.imshow("Black Hat", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()