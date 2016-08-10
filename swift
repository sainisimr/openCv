import cv2
import numpy as np

img = cv2.imread('q.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp)

cv2.imshow('image',img)
cv2.waitKey(q)
cv2.destroyAllWindows()
