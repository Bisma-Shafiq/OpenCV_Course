import cv2

img = cv2.imread("Resources/car.jpg")
print(img.shape)    # (360(H), 640(W), 3 (channel-RGB))
cv2.imshow('OUTPUT',img)

# resize image
img_resize = cv2.resize(img,(300,500))
print(img_resize.shape)
cv2.imshow('RESIZE',img_resize)

#crop image
img_crop= img[0:100,200:278]
print(img_crop.shape)
cv2.imshow('CROP',img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()