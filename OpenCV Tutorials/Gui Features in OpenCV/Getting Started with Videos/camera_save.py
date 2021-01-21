import cv2 as cv
from datetime import datetime
cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
print (time)
out = cv.VideoWriter('%s.avi' %time, fourcc, 20.0, (640,  480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #frame = cv.flip(frame, 0)
    # write the flipped frame
    
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
        
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()