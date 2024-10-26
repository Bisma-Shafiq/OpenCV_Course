import cv2
#  Image Read / Show
image = cv2.imread("Resources/car.jpg")
cv2.imshow("output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Camera Access
cap = cv2.VideoCapture(0)
cap.set(2,220)
cap.set(3,480)
while True:
    success,img = cap.read()
    cv2.imshow('Screen',img)
    if cv2.waitKey(1) & 0xFF== ord('w'):
        break

# Video Play
cap = cv2.VideoCapture('Resources/video.mp4')
while True:
    success,img = cap.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF== ord('w'):
        break
        