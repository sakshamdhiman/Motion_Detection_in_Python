# Motion_Detection_in_Python
### This project was an attempt to execute motion detection in Python using OpenCV.

### Running the project -  
- Download the files, install the libraries(cv2,bokeh,pandas) and execute plotting.py.  
- 3 windows should open (Normal,Delta,Threshold).  
- These will capture the motion in front of the web cam  
- To exit press the key "Q".  
- A graph should appear in the browser with start and end time of motion detection.  

### Project Execution Procedure -
1] Capturing video from webcam and converting it to grayscale.  
2] Forming delta_frame, which is the absolute difference of values between frame matrix of the first captured frame and the current captured frame.  
3] Forming the threshold_frame, which makes delta_frame matrix values>30 equal to 255(white). This makes the area with motion,white on screen, forming contours.  
4] Finding the contours with area > 4000 => motion.  
5] Making a bounding rectangle around the contour.  
6] Appending time on detecting motion.  
7] Displaying the normal, delta and threshold window frames.  
8] Making dataframe for start and end time of motion detection and closing all window frames.  
9] Making a bokeh plot for the start and end time of motion detection using the dataframe generated. Saving the plot in a HTML file.  


