import cv2
import numpy as np
import pandas as pd
import cvlib as cv
from cvlib.object_detection import draw_bbox
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(0)
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
i = 0
# Read until video is completed
while cap.isOpened():
  # Capture frame-by-frame
  ret, frame = cap.read()
  if frame is None:
    print('frame is none')
    break
    # Saving the frames with certain namec
  if ret == True:
    #laplacian_var = cv2.Laplacian(frame, cv2.CV_64F).var()
    box, label, count = cv.detect_common_objects(frame)
    output = draw_bbox(frame, box, label, count)
    #output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
    if (len(label) > 1) or (len(label) == 1 and label[0] != 'bottle'):
        print("incorrect trash, motor 2 open")
    else if(len(label) == 1 and label[0] == 'bottle'):
        print("motor 1 open")
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

 
  # Break the loop
  else: 
    break
  cv2.imshow("test", output)
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
