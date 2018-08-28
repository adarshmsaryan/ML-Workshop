import cv2
import numpy as np
img=cv2.imread("index.jpg")
height,width=img.shape[:2]
rm=cv2.getRotationMatrix2D((width/2,height/2),70,.5)
ri=cv2.warpAffine(img,rm,(width,height))
cv2.imshow('rotated image',ri)
cv2.imshow('original img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
