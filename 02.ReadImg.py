import cv2
img = cv2.imread("Resource/Lenna.png")
print(img.shape)

imgResize = cv2.resize (img, (1000,1000))
print(imgResize.shape)

imgCropped = img [100:300, 100:300]


cv2.imshow("Output",img)
cv2.imshow("Resize",imgResize)
cv2.imshow("Cropped",imgCropped)

cv2.waitKey(0)