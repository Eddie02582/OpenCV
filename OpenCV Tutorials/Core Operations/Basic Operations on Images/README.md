# Basic Operations on Images

## Accessing and Modifying pixel values

code 如下

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

要繪製橢圓，我們需要傳遞幾個參數。 一個參數是中心位置（x，y）。 下一個參數是軸長度（長軸長度，短軸長度）。 角度是橢圓在逆時針方向上的旋轉角度。 startAngle和endAngle表示從主軸順時針方向測量的橢圓弧的起點和終點。 即給出值0和360給出完整的橢圓。 有關更多詳細信息，請查看cv.ellipse（）的文檔。 下面的示例在圖像的中心繪製一個半橢圓。</br>
img	=cv.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]	)
``` python
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
```

## Polygon

要繪製多邊形，首先需要頂點坐標。 將這些點組成一個形狀為ROWSx1x2的數組，其中ROWS是頂點數，它應該是int32類型。 在這裡，我們繪製一個帶有四個黃色頂點的小多邊形。</br>
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)


## Text 

要將文本放入圖像中，您需要指定以下內容。
<ul>
    <li>寫入的文字</li>
    <li>為置座標(左下角)</li>
    <li>字體類型</li>
    <li>字體大小</li>
    <li>一些常見的，如顏色，粗細，線型等。為了更好看，建議使用lineType = cv.LINE_AA。</li>
</ul>


img	=cv.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]	)

``` python
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
```


## Result  
結果如下</br>

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