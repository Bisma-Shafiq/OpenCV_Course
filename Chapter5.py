# WRAP Prespective

import cv2
import numpy as np

img = cv2.imread('Resources/img_1.png')

print(img.shape)  # (539, 359, 3)
width, height = 539,359
pt1 = np.float32 ([[26,348],[321,350],[28,545],[322,545]])
pt2 = np.float32 ([[0,0],[width,0],[0,height],[width, height]])
matrix= cv2.getPerspectiveTransform(pt1,pt2)
output= cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('IMG',img)
cv2.imshow('IMG',output)
cv2.waitKey(0)
cv2.destroyAllWindows()