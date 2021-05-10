# Basic Operations on Images

## Accessing and Modifying pixel values

code �p�U

``` python
import numpy as np
import cv2 as cv
img = cv.imread('messi5.jpg')
```
 
## Rectangle
``` python
#cv2.line(img,pt1 top left ,bot right pt2,color,thickness)
cv.rectangle(img,top-lerf-corner,bottom-right-corner,(0,255,0),3)
```

## Circle
``` python

cv2.circle(img,(447,63),63, (0,0,255), -1)
```

## Ellipse

�nø�s���A�ڭ̻ݭn�ǻ��X�ӰѼơC �@�ӰѼƬO���ߦ�m�]x�Ay�^�C �U�@�ӰѼƬO�b���ס]���b���סA�u�b���ס^�C ���׬O���b�f�ɰw��V�W�����ਤ�סC startAngle�MendAngle��ܱq�D�b���ɰw��V���q����꩷���_�I�M���I�C �Y���X��0�M360���X���㪺���C ������h�ԲӫH���A�Ьd��cv.ellipse�]�^�����ɡC �U�����ܨҦb�Ϲ�������ø�s�@�ӥb���C</br>
img	=cv.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]	)
``` python
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
```

## Polygon

�nø�s�h��ΡA�����ݭn���I���СC �N�o���I�զ��@�ӧΪ���ROWSx1x2���ƲաA�䤤ROWS�O���I�ơA�����ӬOint32�����C �b�o�̡A�ڭ�ø�s�@�ӱa���|�Ӷ��⳻�I���p�h��ΡC</br>
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)


## Text 

�n�N�奻��J�Ϲ����A�z�ݭn���w�H�U���e�C
<ul>
    <li>�g�J����r</li>
    <li>���m�y��(���U��)</li>
    <li>�r������</li>
    <li>�r��j�p</li>
    <li>�@�Ǳ`�����A�p�C��A�ʲӡA�u�����C���F��n�ݡA��ĳ�ϥ�lineType = cv.LINE_AA�C</li>
</ul>


img	=cv.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]	)

``` python
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
```


## Result  
���G�p�U</br>

![image](https://github.com/Eddie02582/OpenCV/blob/master/OpenCV%20Tutorials/Gui%20Features%20in%20OpenCV/Drawing%20Functions%20in%20OpenCV/result.png)



``` python
import cv2

# Create a black image
img = np.zeros((500,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px

#cv2.line(img,pt1,pt2,color,int thickness=1,int line_type=8,int shift=0)
cv2.line(img,(0,0),(511,511),(0,255,0),3)

#cv2.line(img,pt1 top left ,bot right pt2,color,thickness)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

cv2.circle(img,(447,63),63, (0,0,255), -1)

cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#Drawing Polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OPENCV',(10,500),font,4,(255,255,255))


cv2.namedWindow('image')
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
	cv2.destroyAllWindows()
 ``` 