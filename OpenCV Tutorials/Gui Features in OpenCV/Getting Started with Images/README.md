# Getting Started with Images

## 讀取圖片

cv.imread(	filename[, flags]	) </br>
<ul>
    <li>filename:圖片絕對或相對路徑</li>
    <li>指定圖片的方式
    <ul>
        <li>cv.IMREAD_COLOR:加載彩色圖像。 任何圖像的透明度都將被忽略。這是預設</li>
        <li>cv.IMREAD_GRAYSCALE:以灰階模式加載圖像</li>
        <li>cv.IMREAD_UNCHANGED:加載圖像，包括alpha chann </li>    
    </ul>   
    </li>
</ul>

<strong>Note: 以上也可以用數字填入分別代表1,0,-1</strong>

code 如下

``` python
import cv2 as cv
# Load an color image in grayscale
img = cv.imread('pikachu.jpg',0)
```
 
## 顯示影像
使用cv.imshow(winname,img),winname:視窗名稱

cv.waitKey()是一個鍵盤綁定函數。 它的參數是以毫秒為單位的時間。 該函數等待任何鍵盤事件的指定毫秒。 如果您在該時間內按任意鍵，程序將繼續。 如果為0，則無限期等待鍵擊。 它也可以設置為檢測特定的鍵擊
cv.destroyAllWindows() 破壞所有視窗,如果要指定,可在後面代參數

code 如下

``` python
import cv2 as cv

# Load an color image in grayscale
img = cv.imread('pikachu.jpg',0)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
```

有一種特殊情況，您可以在以後創建窗口並將圖像加載到該窗口。 在這種情況下，您可以指定窗口是否可調整大小。 它使用函數cv.namedWindow（）完成。 默認情況下，標誌為cv.WINDOW_AUTOSIZE。 但是如果將flag指定為cv.WINDOW_NORMAL，則可以調整窗口大小。 當圖像尺寸過大並向窗口添加軌跡欄時，它會很有用。


結果如下</br>
<img src = "https://github.com/Eddie02582/OpenCV/blob/master/OpenCV%20Tutorials/Gui%20Features%20in%20OpenCV/Getting%20Started%20with%20Images/show.png">

## Write an image
使用 cv.write(image_filename,mat)
<ul>
    <li>image_filename:名稱</li>
    <li>圖片</li> 
</ul>

我們針測使用者輸入鍵盤,如果是esc 關掉視窗,如果是s 存圖片的動作在關掉視窗

code 如下

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
