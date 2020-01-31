import numpy as np
import cv2
from matplotlib import pyplot as plt

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Error opening video stream")

while capture.isOpened():
    ret, frame = capture.read()
    if ret:

        edges = cv2.Canny(frame, 100, 100)

        cv2.imshow('Frame', frame)
        cv2.imshow('Edges', edges)
        im_ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
        skin_ycrcb_mint = np.array((0, 133, 77))
        skin_ycrcb_maxt = np.array((255, 173, 127))
        skin_ycrcb = cv2.inRange(im_ycrcb, skin_ycrcb_mint, skin_ycrcb_maxt)
        cv2.imshow('Masked', skin_ycrcb)
	# cv2.imwrite(sys.argv[2], skin_ycrcb) # Second image
        contours, _ = cv2.findContours(skin_ycrcb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i, c in enumerate(contours):
            area = cv2.contourArea(c)
            
            if area > 1000:
                cv2.drawContours(frame, contours, i, (255, 0, 0), 3)
                cv2.imshow('Masked 2', frame)         # Final image
       

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()

cv2.destroyAllWindows()

