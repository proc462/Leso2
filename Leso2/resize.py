import cv2

image1 = cv2.imread("Ash.png",1)

cv2.imshow("orignal",image1)

#The order of diemensions is (WIDTH, HEIGHT)
resized = cv2.resize(image1,(2000,950))

cv2.imshow("Resize",resized)

cv2.waitKey(0)
cv2.destroyAllWindows()