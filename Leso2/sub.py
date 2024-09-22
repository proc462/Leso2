import cv2

image1 = cv2.imread("Ash.png")
image2 = cv2.imread("Pikachu.png") 

subImage = cv2.subtract(image1,image2)

cv2.imshow("a",subImage)

cv2.waitKey(0)
cv2.destroyAllWindows()