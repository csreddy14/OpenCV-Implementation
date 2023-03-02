# Filtering images
import cv2
import numpy as np

# import image
img = cv2.imread('my-whole.jpg')

# Form the filters
kernel_identity = np.array([[0,0,0],[0,1,0],[0,0,0]])
kernel_3 = np.ones((3,3), dtype=np.float32) / 9.0
kernel_5 = np.ones((5,5), dtype=np.float32) / 25.0
kernel_11 = np.ones((11,11), dtype=np.float32) / 121.0

# Apply filters
output1 = cv2.filter2D(img, -1, kernel_identity)
output2 = cv2.filter2D(img, -1, kernel_3)
output3 = cv2.filter2D(img, -1, kernel_5)
output4 = cv2.filter2D(img, -1, kernel_11)

# Show the images
cv2.imshow("Same", output1)
cv2.imshow("3 blur", output2)
cv2.imshow("5 blur", output3)
cv2.imshow("11 blur", output4)

cv2.waitKey(0)
cv2.destroyAllWindows()