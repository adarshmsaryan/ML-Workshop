import cv2
import numpy as np
img=cv2.imread('index.jpg')
cv2.imshow('original',img)
cv2.waitKey(0)
m=np.ones(img.shape,dtype="uint8")*150
added=cv2.add(img,m)
cv2.imshow('added',added)
subtract=cv2.subtract(img,m)
cv2.imshow('subtract',subtract)
mul=cv2.multiply(img,m)
cv2.imshow('mul',mul)
cv2.waitKey(0)
cv2.destroyAllWindows()

