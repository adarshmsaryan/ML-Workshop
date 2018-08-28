import cv2
import numpy as np
img=cv2.imread("index.jpg")
height,width=img.shape[:2]
print(height)
print(width)
qh,qw=height/4,width/4
print(qh)
print(qw)
t=np.float32([[1,0,qw],[0,1,qh]])
print(t)
img_translation=cv2.warpAffine(img,t,(width,height))
cv2.imshow('original img',img)
cv2.imshow('Traslated',img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
