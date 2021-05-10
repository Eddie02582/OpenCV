# Getting Started with Images

## Ū���Ϥ�

cv.imread(	filename[, flags]	) </br>
<ul>
    <li>filename:�Ϥ�����ά۹���|</li>
    <li>���w�Ϥ����覡
    <ul>
        <li>cv.IMREAD_COLOR:�[���m��Ϲ��C ����Ϲ����z���׳��N�Q�����C�o�O�w�]</li>
        <li>cv.IMREAD_GRAYSCALE:�H�Ƕ��Ҧ��[���Ϲ�</li>
        <li>cv.IMREAD_UNCHANGED:�[���Ϲ��A�]�Aalpha chann </li>    
    </ul>   
    </li>
</ul>

<strong>Note: �H�W�]�i�H�μƦr��J���O�N��1,0,-1</strong>

code �p�U

``` python
import cv2 as cv
# Load an color image in grayscale
img = cv.imread('pikachu.jpg',0)
```
 
## ��ܼv��
�ϥ�cv.imshow(winname,img),winname:�����W��

cv.waitKey()�O�@����L�j�w��ơC �����ѼƬO�H�@����쪺�ɶ��C �Ө�Ƶ��ݥ�����L�ƥ󪺫��w�@��C �p�G�z�b�Ӯɶ��������N��A�{�ǱN�~��C �p�G��0�A�h�L�������������C ���]�i�H�]�m���˴��S�w������
cv.destroyAllWindows() �}�a�Ҧ�����,�p�G�n���w,�i�b�᭱�N�Ѽ�

code �p�U

``` python
import cv2 as cv

# Load an color image in grayscale
img = cv.imread('pikachu.jpg',0)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
```

���@�دS���p�A�z�i�H�b�H��Ыص��f�ñN�Ϲ��[����ӵ��f�C �b�o�ر��p�U�A�z�i�H���w���f�O�_�i�վ�j�p�C ���ϥΨ��cv.namedWindow�]�^�����C �q�{���p�U�A�лx��cv.WINDOW_AUTOSIZE�C ���O�p�G�Nflag���w��cv.WINDOW_NORMAL�A�h�i�H�վ㵡�f�j�p�C ��Ϲ��ؤo�L�j�æV���f�K�[�y����ɡA���|�ܦ��ΡC


���G�p�U</br>
<img src = "https://github.com/Eddie02582/OpenCV/blob/master/OpenCV%20Tutorials/Gui%20Features%20in%20OpenCV/Getting%20Started%20with%20Images/show.png">

## Write an image
�ϥ� cv.write(image_filename,mat)
<ul>
    <li>image_filename:�W��</li>
    <li>�Ϥ�</li> 
</ul>

�ڭ̰w���ϥΪ̿�J��L,�p�G�Oesc ��������,�p�G�Os �s�Ϥ����ʧ@�b��������

code �p�U

``` python
import numpy as np
import cv2 as cv

img = cv.imread('pikachu.jpg',0)
cv.imshow('image',img)
k = cv.waitKey(0) 
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('pikachu.png',img)
    cv.destroyAllWindows()
k = cv.waitKey(0)
```

## Using Matplotlib

``` python
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('messi5.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
```
