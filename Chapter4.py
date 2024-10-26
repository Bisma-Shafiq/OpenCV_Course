import cv2
import numpy as np

img = np.zeros((500,500,3),np.uint8)
print(img)
img[:] = 78,67,55   # to make whole image gray

#  draw line
cv2.line(img,(0,0),(230,330),(234,145,45),5)
#cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(234,145,45),5)   # for complete diagnol line

#draw rectangle
cv2.rectangle(img,(263,445),(25,56),(45,78,255),5)

# draw circle
cv2.circle(img,(240,290),45,(0,255,0),cv2.FILLED)

# Put text
cv2.putText(img, "OPENCV TUTORIAL",(125,67),cv2.FONT_ITALIC,1,(1,150,0),1)

# Output
cv2.imshow('OUTPUT',img)
cv2.waitKey(0)
cv2.destroyAllWindows()