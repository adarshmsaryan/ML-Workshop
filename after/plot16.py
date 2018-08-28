import cv
import matplotlib.pyplot as plt
'''import numpy as np
img=cv2.imread("index.jpg")
red=img(HSV[:,:,2])
green=img[:,:,1]
blue=img[:,:,0]
#gray=cv2.cvtColor(img,cv2.COLOR_RG)
RGB=['r','g','b']
cv2.imshow("MS DHONI1 red",imag)
cv2.imshow("MS DHONI2 green",img)
cv2.imshow("MS DHONI3 blue",img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
mat src=imread("index.jpg",CV_LOAD_COLOR);
mat bgr[3];
split(src.bgr);
imwrite("blue.png",bgr[0]);
imwrite("red.png",bgr[1]);
imwrite("green.png",bgr[2]);
cv2.waitKey(0)
cv2.destroyAllWindows()
