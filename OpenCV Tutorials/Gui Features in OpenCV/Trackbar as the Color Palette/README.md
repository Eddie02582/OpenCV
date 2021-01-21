# Trackbar as the Color Palette

## Code Demo

我們將創建一個簡單的應用程序，顯示您指定的顏色。您有一個顯示顏色的窗口和三個軌道欄，用於指定B，G，R顏色。您可以滑動軌跡欄並相應地窗口顏色更改。默認情況下，初始顏色將設置為黑色。</br>

對於cv.getTrackbarPos（）函數，第一個參數是軌道欄名稱，第二個參數是它所附加的窗口名稱，第三個參數是默認值，第四個參數是最大值，第五個參數是執行的回調函數每次軌跡欄值都會發生變化。回調函數始終具有默認參數，即軌跡欄位置。在我們的例子中，函數什麼都不做，所以我們簡單地通過。</br>

軌跡欄的另一個重要應用是將其用作按鈕或開關。默認情況下，OpenCV沒有按鈕功能。因此，您可以使用跟?欄來獲得此類功能。在我們的應用程序中，我們創建了一個開關，其中應用程序僅在開關打開時有效，否則屏幕始終為黑色。</br>

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
 












