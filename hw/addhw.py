import cv2

image1 = cv2.imread("brokencar.png",1)
image2 = cv2.imread("Shiva.png",1)

addImage = cv2.addWeighted(image1,0.5,image2,0.4,0)

#0.5 and 0.4 are wieghts to be multiplied for each pixel,
#0 is gamma_value (measurement of light)

cv2.imshow("thing",addImage)

cv2.waitKey(0)
cv2.destroyAllWindows()