import cv2
import numpy as np
img=np.ones((255,255,3),np.uint8)*255
cv2.imshow('Black Rectangle(Color)',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
