import cv2
import numpy as np

img = cv2.imread('a.jpg', cv2.IMREAD_COLOR)

cv2.rectangle(img, (25,80),(200,200),(0,255,0),5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Letter A', (50,190),font,1,(200,255,255),2,cv2.LINE_AA)

#Displays the image and everything I drew on it 
cv2.imshow('image',img)

#Waits for any key to be pressed
cv2.waitKey(0)
cv2.destroyAllWindows()#If button pressed windows destroyed


