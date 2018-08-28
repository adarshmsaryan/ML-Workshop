import cv2
import numpy as np
sqr=np.zeros((300,300),np.uint8)
cv2.rectangle(sqr,(50,50),(250,250),255,-1)
cv2.imshow("square",sqr)

ellipse=np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("ellipse",ellipse)
cv2.waitKey(0)

And=cv2.bitwise_and(sqr,ellipse)
cv2.imshow("AND",And)
cv2.waitKey(0)
 
Or=cv2.bitwise_or(sqr,ellipse)
cv2.imshow("OR",Or)
cv2.waitKey(0)
 
ex=cv2.bitwise_xor(sqr,ellipse)
cv2.imshow("EXOR",ex)
cv2.waitKey(0)
 
Not=cv2.bitwise_not(sqr)
cv2.imshow("AND",Not)
cv2.waitKey(0)
cv2.destrouAllWindows()
