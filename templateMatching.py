import cv2
import numpy as np


def recognise(img, lookingFor):

    img_rgb = cv2.imread(img)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread(lookingFor,0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

    cv2.imshow('Detected',img_rgb)



    cv2.imshow('Detected',img_rgb)
#recognise('blueB.jpg','bluerA.jpg')

    
def recognize(img):
    img = cv2.imread(img,600)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #The color of my glove
    lower_blue = np.array([80,90,100])
    upper_blue = np.array([170,170,250])

    #Makes everything except anything that is the same color
    #as my glove black 
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(img,img, mask= mask)

    kernel = np.ones((5,5), np.uint8)

    #This is to reduce the noise in the background
    erosion = cv2.erode(mask, kernel, iterations = 1)

    dilation = cv2.dilate(mask, kernel, iterations = 1)
    

    #I want to find the extreme contours of my hand.
    image,contours, hierachy = cv2.findContours(erosion,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #print("Contours")
    #for i in range(len(contours)):
        #print("Contour",i,"points:",len(contours[i]))

    cv2.imshow('Detected',img)
    cv2.imshow('res',
               res)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
        
        #This calculates the convex points (tips of fingers)
    #and the defects the deep points on the fingers which
    #should help me to understand how many fingers are
    #up
    try:
        cnt = contours[0]
        #print(cnt)

        hull = cv2.convexHull(cnt, returnPoints = True)
        #print("hull are",hull)
        return hull

        #defects returns an array with start,end,farthest point,distanceToFarthest point
        defects = cv2.convexityDefects(cnt,hull)
        #print("defects are",defects)
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            cv2.line(img,start,end,[0,255,0],2)
            cv2.circle(img,far,5,[0,0,255],-1)
            print(defects)
        

    except:
        pass
    
    #cv2.imshow('img',img)
    #cv2.imshow('res',res)
    #cv2.imshow('erosion',erosion)


recognize("4_3.jpg")

