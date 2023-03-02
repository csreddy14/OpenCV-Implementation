import cv2
# read, write, display and save operations
# print(cv2.__version__)

img = cv2.imread('my-whole.jpg',0) # 0 gives the grey scale version of our image

cv2.imshow('Image',img)
cv2.imwrite('greySpace.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
