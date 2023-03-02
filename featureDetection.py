# Feature detection
import cv2
import argparse
import numpy as np
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="taj.jpg", help="path to input image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Harris Corner detection
harrisCorner = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.03)

# dilate to mark the corners
harrisCorner = cv2.dilate(harrisCorner, None)
img[harrisCorner > 0.01 * harrisCorner.max()] = [0, 255, 0]
cv2.imshow('haris_corner', img)


# Shi-Tomasi corner detection
ShiTCorners = cv2.goodFeaturesToTrack(gray, maxCorners=50, qualityLevel=0.02, minDistance=20)
ShiTCorners = np.float32(ShiTCorners)
  
for item in ShiTCorners:
    x, y = item[0]
    x = int(x)
    y = int(y)
    cv2.circle(img, (x, y), 6, (0, 255, 0), -1)

cv2.imshow('good_features', img)

# SIFT (Scale-Invariant Feature Transform)
# sift = cv2.SIFT_create()
# kp, des = sift.detectAndCompute(gray, None)

# kp_image = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.imshow('SIFT', kp_image)

# FAST algorithm for corner detection
fast = cv2.FastFeatureDetector_create()
# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))

# Print all default params
print( "Threshold: {}".format(fast.getThreshold()) )
print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
print( "neighborhood: {}".format(fast.getType()) )
print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )
cv2.imwrite('fast_true.png', img2)

# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img, None)
print( "Total Keypoints without nonmaxSuppression: {}".format(len(kp)) )
img3 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))
cv2.imshow('FAST', img3)


# ORB (Oriented FAST and Rotated Brief)
# Initiate ORB detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kpOrb = orb.detect(img,None)

# compute the descriptors with ORB
kpOrb, desOrb = orb.compute(img, kpOrb)
imgOrb = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
cv2.imshow("ORB", imgOrb)
plt.imshow(imgOrb), plt.show()


# SURF (Speeded-Up Robust Features)
surf = cv2.xfeatures2d.SURF_create()
kpSurf, desSurf = surf.detectAndCompute(gray, None)

kpSurf_img = cv2.drawKeypoints(img, kpSurf, None, color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SURF', kpSurf_img)

cv2.waitKey(0)
cv2.destroyAllWindows