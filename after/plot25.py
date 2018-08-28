import cv2
import numpy as np
img=cv2.imread("index.jpg")
ri=cv2.transpose(img,70)
cv2.imshow('rotated image',ri)
cv2.imshow('original img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
