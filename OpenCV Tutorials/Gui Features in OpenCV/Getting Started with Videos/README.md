# Getting Started with Videos

## �����v���e��


``` python
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
        
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
```
 

cv.VideoCapture(position):position����v����m,�q�`�b�u���@�x��v����0,�ĤG�x�O1....</br>
cap.read() �^�Ǩ�ӰѼ�(ret,frame),ret �O��bool(True/False),��ܬO�_���\Ū��,frame�N�O��ܵe��</br>
cv.cvtColor(frame, cv.COLOR_BGR2GRAY):�ĤG�ӰѼ��C���ഫ��flag</br>
cap.release():������v��</br>
cap.set(propId, value):�]�w�Ѽ�,propId�N���P���]�w,propId=3��ܳ]�w�e��cap.set(3,width)...,�Բӥi�H�Ѧ�<a href="https://docs.opencv.org/4.1.0/d4/d15/group__videoio__flags__base.html#ggaeb8dd9c89c10a5c63c139bf7c4f5704dad8b57083fd9bd58e0f94e68a54b42b7e">VideoCaptureProperties</a>


## �x�s�v��

�o���ڭ̳Ыؤ@��VideoWriter��H�C �ڭ����ӫ��w��X���W�]�Ҧp�Goutput.avi�^�C �M��ڭ����ӫ��wFourCC�N�X�]�U�@�q�����Ӹ`�^�C �M�����ǻ��C��V�ơ]fps�^�M�V�j�p�C �̫�@�ӬOisColor�лx�C �p�G�OTrue�A�h�s�X���ݭn�m��V�A�_�h���A�Ω�ǫ״V�C</br>

FourCC�O�@��4�r�`�N�X�A�Ω���w���W�s�ѽX���C �i�bfourcc.org�����i�ΥN�X�C��C �����M�󥭥x�C �H�U�s�ѽX����ڨӻ��ܦn�C</br>
<ul>
    <li>Fedora�GDIVX�AXVID�AMJPG�AX264�AWMV1�AWMV2�C</li>
    <li>In Windows: DIVX (More to be tested and added)</li>
    <li>In OSX: MJPG (.mp4), DIVX (.avi), X264 (.mkv).</li>
</ul>

``` python
import cv2 as cv

cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame, 0)
    # write the flipped frame
    
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
        
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows(
```

## Ū���v��

���P�q�۾�����ۦP�A�u�ݥε��W���W���۾����ާY�i�C �P�ɦb��ܴV�ɡA�Ь�cv.waitKey()�ϥξA���ɶ��C �p�G���Ӥp�A���W�N�D�`�֡A�p�G���Ӱ��A���W�N�|�ܺC�]��A�o�N�O�A�i�H�κC�ʧ@��ܵ��W�^�C ���`���p�U�A25�@��N�i�H�F�C

``` python
import cv2 as cv
cap = cv.VideoCapture('vtest.avi')

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
        
cap.release()
cv.destroyAllWindows()
```











