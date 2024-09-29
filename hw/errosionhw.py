import cv2
import numpy as np 

img=cv2.imread("brokencar.png")
cv2.imshow("Original",img)

kernal=np.ones((5,5), np.uint8)
print(kernal)

erosion=cv2.erode(img,kernal)
print(kernal)

erosion=cv2.erode(img,kernal)

cv2.imshow("Eroded Image", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()