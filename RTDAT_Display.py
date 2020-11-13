import numpy 
import cv2 
import datetime as dt
vid = cv2.VideoCapture(0)  
while(vid.isOpened()): 
    ret, frame = vid.read() 
  
    if ret: 
        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX 
        d_t = str(dt.datetime.now()) 
        frame = cv2.putText(frame, d_t, 
                            (10, 100), 
                            font, 0.8, 
                            (210, 155, 155),  
                            4, cv2.LINE_8) 
        cv2.imshow('frame', frame) 
  
        key = cv2.waitKey(1) 
        if key == 'q' or key == 27: 
            break
    else: 
          
        break
vid.release()
cv2.destroyAllWindows() 