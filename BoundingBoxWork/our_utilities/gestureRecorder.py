import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if (cap.isOpened()== False):
    print("Error opening video stream")

id_counter = 0
started = False
recording = False

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)

        if recording and not started:
            out = cv2.VideoWriter('wave_' + str(id_counter) + '.mp4', 0x7634706d, 10, (frame_width,frame_height))
            started = True

        if recording:
            out.write(frame)

        if cv2.waitKey(25) & 0xFF == ord('d') and recording:
            print("Done recording")
            recording = False
            started = False

        if cv2.waitKey(25) & 0xFF == ord('c') and not started:
            print("Starting recording")
            id_counter += 1
            recording = True
            started = False

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()
