import cv2
import numpy as np
import matplotlib.pyplot as plt

#The final project should
#[1] explore an area of robotics that is of interest to you
#[2] build on some aspect of the technical/theoretical knowledge gained in the class so far,
#[3] involve reviewing at least one robotics research paper,
#[4] result in a working implementation that can be demonstrated."


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #The color of my glove
    lower_blue = np.array([80,80,100])
    upper_blue = np.array([180,180,250])

    #Makes everything except anything that is the same color
    #as my glove black 
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    kernel = np.ones((5,5), np.uint8)

    #This is to reduce the noise in the background
    erosion = cv2.erode(mask, kernel, iterations = 1)
    

    #I want to find the extreme contours of my hand.
    image,contours, hierachy = cv2.findContours(erosion,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
   
    #This calculates the convex points (tips of fingers)
    #and the defects the deep points on the fingers which
    #should help me to understand how many fingers are
    #up
    try:
        cnt = contours[0]
        print(cnt)

        hull = cv2.convexHull(cnt, returnPoints = False)

        #defects returns an array with start,end,farthest point,distanceToFarthest point
        defects = cv2.convexityDefects(cnt,hull)
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            cv2.line(frame,start,end,[0,255,0],2)
            cv2.circle(frame,far,5,[0,0,255],-1)

    except:
        pass
    
    #cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
         break

cv2.destroyAllWindows()
cap.release()


 
