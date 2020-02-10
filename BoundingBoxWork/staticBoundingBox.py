import cv2
import numpy as np

input_stream = cv2.VideoCapture(0)

if (input_stream.isOpened() == False):
    print("Error opening video stream")

frame_width = int(input_stream.get(3))
frame_height = int(input_stream.get(4))


print(str(frame_width) +  " = width")
print(str(frame_height) + " = height")
min_width = int(frame_width * .33)
max_width = int(frame_width * .66)
min_height = int(frame_height * .33)
max_height = int(frame_height * .66)


print("mnw: " + str(min_width) + "mxw: " + str(max_width) + " mnh: " + str(min_height) + " mxh: " + str(max_height)) 
while (input_stream.isOpened()):
    ret, frame = input_stream.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        # cv2.rectangle(frame, ((frame_width * .33), (frame_height * .33)), ((frame_width * .66), (frame_height * .66)), (77, 255, 9), 1)
        
        # Switched to only using width to allow for a square region
        bounded = cv2.rectangle(frame, (min_width,min_width), (max_width,max_width), (0, 255, 0), 2)
        cv2.imshow('Bounded', bounded)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

input_stream.release()
cv2.destroyAllWindows()



