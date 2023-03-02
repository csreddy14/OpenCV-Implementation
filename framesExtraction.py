# Extracting frames from video
import cv2

vid = cv2.VideoCapture(r'C:\Users\chant\OneDrive\Desktop\OpenCV\Resources/vid1.mp4')
currentFrame = 0

while(True):
    suc, frm = vid.read()

    cv2.imshow("Output", frm)
    cv2.imwrite('./Extracted/frame'+str(currentFrame) + '.jpg', frm) # Extracted frames will go into the "Extracted" folder and images are saved as frame1, frame, frame3....
    currentFrame += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()