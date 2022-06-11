import cv2

img = cv2.imread("son.jpeg",)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("ORIGINAL IMAGE", img)
cv2.imshow("IMAGE GRAYSCALE", gray)

cv2.waitKey(0)
cv2.destroyAllWindow()
