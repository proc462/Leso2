import cv2
import numpy as np 

img=cv2.imread("Pikachu.png")
cv2.imshow("Original",img)

#filter 3*3, 5*5 - Kernal
#kernal/filter is used for erosion as an input
#uint8 - unsigned interger og 8 bit

kernal=np.ones((5,5), np.uint8)
print(kernal)

erosion=cv2.erode(img,kernal)
print(kernal)

erosion=cv2.erode(img,kernal)

cv2.imshow("Eroded Image", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

