from cv2 import cv2
import time
from datetime import datetime as dt
import pandas

first_frame = None
video = cv2.VideoCapture(0)                         #0 to pass the web cam for video
status_list=[None,None]
time=[]
v_frame = 0
df = pandas.DataFrame(columns=["Start","End"])
while True:
    status = 0
    check, frame = video.read()                     #video.read() returns a tuple with two values. The first one is a boolean indicating whether the frame was captured or not, while the second gives the actual frame object.
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   #converting to gray scale
    gray = cv2.GaussianBlur(gray, (21,21),0)
    
    if first_frame is None or v_frame == 0:                         #passing the first frame
        first_frame = gray
        v_frame = 500
        continue                                    
    
    v_frame -= 1
    delta_frame = cv2.absdiff(first_frame,gray)     #Calculates the per-element absolute difference between two arrays or between an array and a scalar
    thresh_frame = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1] #if there is a difference of more than 30 units in pixel value make it 255(white)
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)# dilating the thresh_frame to make contours more prominent

    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #forming outer contours after removing redundent points (like extra points on a line)
    for contours in cnts:
        if cv2.contourArea(contours) < 4000:        #if the white countour area is more than 4000 status=1 => motion detection 
            continue
        status = 1
        (x,y,w,h) = cv2.boundingRect(contours)      #rectangle for motion
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)

    status_list = status_list[-2:]                  #appending time of motion detection
    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:
        time.append(dt.now())
    if status_list[-1]==0 and status_list[-2]==1:
        time.append(dt.now())
    cv2.imshow("Normal", frame)                  #displaying the video captured window
    cv2.imshow("Delta", delta_frame)
    cv2.imshow("Threshold", thresh_frame)
    
    key = cv2.waitKey(1)                            #waiting for 1ms and going to the next frame
    print(gray)
    
    if key==ord('q'):                               #defining a quiting path on pressing "q"
        if status == 1:
            time.append(dt.now())
        break

print(status_list)
print(time)

for i in range(0,len(time),2):                      #making the dataframe for motion detection time
    df = df.append({"Start":time[i],"End":time[i+1]},ignore_index=True)
df.to_csv("Times.csv")
                      
video.release()                                     #stopping the capture of the video
cv2.destroyAllWindows()                             #destroying the window

print(df)