# Object Tracking
import cv2
from tracker import *

# create tracker object
tracker = EuclideanDistTracker()

vid = cv2.VideoCapture("highway.mp4")

# object detection from stable camera
obj_det = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    ret, frame = vid.read()
    height, width, _ = frame.shape

    # Extract region of interest
    roi = frame[340:720,500:800]

    # 1. object detection
    mask = obj_det.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in contours:
        # calculate area and remove small elements
        ar = cv2.contourArea(cnt)
        if ar>100:
            # cv2.drawContours(roi, [cnt], -1, (0,255,0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0,255,0), 3)
            print(x, y, w, h)

            detections.append([x, y, w, h])
    

    # 2. object tracking
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0 ,0), 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)


    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("ROI", roi)

    key = cv2.waitKey(30)
    if key == 27:
        break

vid.release()
cv2.destroyAllWindows()