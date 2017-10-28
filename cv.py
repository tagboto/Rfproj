import cv2
import numpy as np


#Reading in a particular image
#convert to grayscale because its easier and faster to read
#img = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('a.jpg', cv2.IMREAD_COLOR)
#cv2.line(img, (0,0),(150,150),(255,255,255),15)


cv2.rectangle(img, (25,80),(200,200),(0,255,0),5)
#cv2.circle(img, (100,63),55,(0,0,255),-1)

#pts = np.array([[10,5],[20,30],[30,20],[50,10]],np.int32)
#pts = pts.reshape((-1,1,2))

#cv2.polylines(img,[pts],True, (0,255,255),3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Letter A', (50,190),font,1,(200,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)
#Waits for any key to be pressed
cv2.waitKey(0)
cv2.destroyAllWindows()#If button pressed windows destroyed

#cv2.imwrite('Agray.png',img)
