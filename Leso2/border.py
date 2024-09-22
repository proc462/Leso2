import cv2

ash=cv2.imread("Ash.png",1)

#cv2.copyMakeBorder(image,top,bottom,left,right,bordertype, colourValue)
borderedImage = cv2.copyMakeBorder(ash,10,10,10,10,cv2.BORDER_CONSTANT, value=1)

cv2.imshow("bord",borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""There are seven types of borders in OpenCV:
BORDER_CONSTANT: This type of border adds a constant value to all the pixels in the border. The value is specified by the 'value' argument.
BORDER_REPLICATE: This type of border replicates the pixels at the edge of the image to fill the border.
BORDER_REFLECT: This type of border reflects the pixels at the edge of the image to fill the border.
BORDER_WRAP: This type of border wraps the pixels at the edge of the image to fill the border.
BORDER_DEFAULT: This type of border uses the default border type, which is BORDER_REPLICATE.
BORDER_ISOLATED: This type of border isolates the image from the border.
BORDER_TRANSPARENT: This type of border makes the border transparent."""

