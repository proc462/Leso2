import cv2

image1 = cv2.imread("brokencar.png",1)

cv2.imshow("orignal",image1)

#The order of diemensions is (WIDTH, HEIGHT)
resized = cv2.resize(image1,(1500,1000))

cv2.imshow("Resizebrokencar",resized)

cv2.waitKey(0)
cv2.destroyAllWindows()