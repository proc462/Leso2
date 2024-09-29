import cv2

image1 = cv2.imread("brokencar.png")
image2 = cv2.imread("Shiva.png") 

subImage = cv2.subtract(image1,image2)

cv2.imshow("thinginverse",subImage)

cv2.waitKey(0)
cv2.destroyAllWindows()