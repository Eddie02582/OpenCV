import numpy as np
import cv2
import sys

if len(sys.argv[1:])==1:

	cap = cv2.VideoCapture(sys.argv[1])

	while(cap.isOpened()):
    # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
            
	cap.release()
	cv2.destroyAllWindows()
