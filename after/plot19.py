import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv2.imshow('original image',img)
cv2.rectangle(img,(100,100),(300,250),(255,255,255),-5)
cv2.imshow('rectangle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
