# importing PIL Module
from PIL import Image
import cv2
import PIL

# open the original image
original_img = Image.open("cars.jfif")

# Flip the original image verticaly
vertical_img = original_img.transpose(method=Image.FLIP_TOP_BOTTOM)
vertical_img.save("vertical.png")

# Load our input image
image = cv2.imread('cars.jfif')
cv2.imshow('Original', image)
cv2.waitKey()

# We use cvtColor, to convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

# window shown waits for any key pressing event
cv2.destroyAllWindows()


# close all our files object
original_img.close()
vertical_img.close()
