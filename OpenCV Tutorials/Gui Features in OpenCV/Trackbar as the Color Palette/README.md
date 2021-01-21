# Trackbar as the Color Palette

## Code Demo

�ڭ̱N�Ыؤ@��²�檺���ε{�ǡA��ܱz���w���C��C�z���@������C�⪺���f�M�T�ӭy�D��A�Ω���wB�AG�AR�C��C�z�i�H�ưʭy����ì����a���f�C����C�q�{���p�U�A��l�C��N�]�m���¦�C</br>

���cv.getTrackbarPos�]�^��ơA�Ĥ@�ӰѼƬO�y�D��W�١A�ĤG�ӰѼƬO���Ҫ��[�����f�W�١A�ĤT�ӰѼƬO�q�{�ȡA�ĥ|�ӰѼƬO�̤j�ȡA�Ĥ��ӰѼƬO���檺�^�ը�ƨC���y����ȳ��|�o���ܤơC�^�ը�Ʃl�ר㦳�q�{�ѼơA�Y�y�����m�C�b�ڭ̪��Ҥl���A��Ƥ��򳣤����A�ҥH�ڭ�²��a�q�L�C</br>

�y���檺�t�@�ӭ��n���άO�N��Χ@���s�ζ}���C�q�{���p�U�AOpenCV�S�����s�\��C�]���A�z�i�H�ϥθ�?�����o�����\��C�b�ڭ̪����ε{�Ǥ��A�ڭ̳ЫؤF�@�Ӷ}���A�䤤���ε{�ǶȦb�}�����}�ɦ��ġA�_�h�̹��l�׬��¦�C</br>

``` python
import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()
```
 












