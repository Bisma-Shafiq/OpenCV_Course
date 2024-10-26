import cv2
import numpy as np


image = cv2.imread("Resources/car.jpg")
kernel = np.ones((6,7),np.uint8)
img_gry = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
img_blr = cv2.GaussianBlur(img_gry,(7,7),0)
img_canny = cv2.Canny(image, 20,89)
img_dilation = cv2.dilate(img_canny,kernel, iterations=1)
cv2.imshow('OUTPUT',image)
cv2.imshow('GRAY',img_gry)
cv2.imshow('BLUR',img_blr)
cv2.imshow('Canny',img_canny)
cv2.imshow('Dilation',img_dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
