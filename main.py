import pytesseract
import cv2
import numpy as mp
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img=cv2.imread('1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))


# ### Detecting Characters
# hT,wT,_=img.shape
# boxes=pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     b=b.split(' ')
#     # print(b)
#     x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img,(x,hT-y),(w,hT-h),(255,0,255),3)
#     cv2.putText(img,b[0],(x,hT-y+30),cv2.FONT_HERSHEY_COMPLEX,1,(255,10,10),1)
#

# ### Detecting Words
# hT,wT,_=img.shape
# boxes=pytesseract.image_to_data(img)
# # print(boxes)
# for x,b in enumerate(boxes.splitlines()):
#     if x==0:
#         continue
#     b=b.split()
#     if len(b)!=12:
#         continue
#     print(b)
#     x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),3)
#     cv2.putText(img,b[11],(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,10,10),1)

### Detecting only Numbers
hT,wT,_=img.shape
conf = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img,config=conf)
for b in boxes.splitlines():
    b=b.split(' ')
    # print(b)
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hT-y),(w,hT-h),(255,0,255),3)
    cv2.putText(img,b[0],(x,hT-y+30),cv2.FONT_HERSHEY_COMPLEX,1,(255,10,10),1)



cv2.imshow('img', img)
cv2.waitKey(0)