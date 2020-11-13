import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.rectangle(frame,(10,12),(3000,3000),(0,255,0),1)
    font=cv2.FONT_HERSHEY_SIMPLEX
    s='dsfhusdhfsgfjsgfdsjf'
    cv2.putText(frame,s,(0,135),font,1,(0,0,0),2,cv2.LINE_AA)
    #            imgage,text,font,whole text size,color,thicc,   )
    cv2.imshow("ot",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyWindow()
