import cv2

ash=cv2.imread("brokencar.png",1)

#cv2.copyMakeBorder(image,top,bottom,left,right,bordertype, colourValue)
borderedImage = cv2.copyMakeBorder(ash,10,10,10,10,cv2.BORDER_WRAP, value=1)

cv2.imshow("bord",borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()