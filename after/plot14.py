import cv2
img=cv2.imread("index.jpg")
img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv image',img_HSV)
cv2.imshow('hue channel',img_HSV[:,:,0])
cv2.imshow('saturation',img_HSV[:,:,1])
cv2.imshow('value channel',img_HSV[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()

