import cv2
import numpy as pd
img=cv2.imread("index.jpg")
h,w=img.shape[:2]

start_row1,start_col1=int(h*.1),int(w*.1)
start_row2,start_col2=int(h*.25),int(w*.25)
start_row3,start_col3=int(h*.50),int(w*.50)
start_row4,start_col4=int(h*.75),int(w*.5)

end_row1,end_col1=int(h*.25),int(w*.25)
end_row2,end_col2=int(h*.50),int(w*.50)
end_row3,end_col3=int(h*.75),int(w*.75)
end_row4,end_col4=int(h*1.0),int(w*1.0)

cropped1=img[start_row1:end_row1,start_col1:end_col1]
cropped2=img[start_row2:end_row2,start_col2:end_col2]
cropped3=img[start_row3:end_row3,start_col3:end_col3]
cropped4=img[start_row4:end_row4,start_col4:end_col4]
cv2.imshow('original',img)
#cv2.waitKey(0)
cv2.imshow('croped1',cropped1)
#cv2.waitKey(0)
cv2.imshow('croped2',cropped2)
#cv2.waitKey(0)
cv2.imshow('croped3',cropped3)
#cv2.waitKey(0)
cv2.imshow('croped4',cropped4)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''print(img.shape)
print("height of the image:",int(img.shape[0]),"pixels")
print("Width of the image:",int(img.shape[0]),"pixels")
cv2.imshow("output.jpg",img)
cv2.imshow("output.png",img)
cv2.destroyAllWindows()'''

