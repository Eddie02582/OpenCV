# Getting Started with Videos

## 抓取攝影機畫面


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
 

cv.VideoCapture(position):position為攝影機位置,通常在只有一台攝影機時0,第二台是1....</br>
cap.read() 回傳兩個參數(ret,frame),ret 是個bool(True/False),表示是否成功讀取,frame就是顯示畫面</br>
cv.cvtColor(frame, cv.COLOR_BGR2GRAY):第二個參數顏色轉換的flag</br>
cap.release():釋放攝影機</br>
cap.set(propId, value):設定參數,propId代表不同的設定,propId=3表示設定寬度cap.set(3,width)...,詳細可以參考<a href="https://docs.opencv.org/4.1.0/d4/d15/group__videoio__flags__base.html#ggaeb8dd9c89c10a5c63c139bf7c4f5704dad8b57083fd9bd58e0f94e68a54b42b7e">VideoCaptureProperties</a>


## 儲存影像

這次我們創建一個VideoWriter對象。 我們應該指定輸出文件名（例如：output.avi）。 然後我們應該指定FourCC代碼（下一段中的細節）。 然後應傳遞每秒幀數（fps）和幀大小。 最後一個是isColor標誌。 如果是True，則編碼器需要彩色幀，否則它適用於灰度幀。</br>

FourCC是一個4字節代碼，用於指定視頻編解碼器。 可在fourcc.org中找到可用代碼列表。 它取決於平台。 以下編解碼器對我來說很好。</br>
<ul>
    <li>Fedora：DIVX，XVID，MJPG，X264，WMV1，WMV2。</li>
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

## 讀取影片

它與從相機捕獲相同，只需用視頻文件名更改相機索引即可。 同時在顯示幀時，請為cv.waitKey()使用適當的時間。 如果它太小，視頻將非常快，如果它太高，視頻將會很慢（嗯，這就是你可以用慢動作顯示視頻）。 正常情況下，25毫秒就可以了。

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











