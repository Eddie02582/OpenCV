import cv2
import ConfigParser




def Config(path,section,name):
	cf = ConfigParser.ConfigParser()
	cf.read(path) 
	return cf.get(section,name)	

port =Config('camera.ini','camera','port')	
width=Config('camera.ini','camera','width')	
height=Config('camera.ini','camera','height')	
	
cap = cv2.VideoCapture(int(port))	

if not cap.isOpened():
    print("Cannot open camera")
    exit()

cap.set(3,int(width))

cap.set(4,int(height))

while True: 
	ret, frame = cap.read() 
	if ret:
		cv2.imshow('frame', frame) 
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()