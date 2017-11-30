# Image Blending

import cv2

img1 = cv2.imread('img_1.jpg')
img2 = cv2.imread('img_2.jpg')
dst = cv2.addWeighted(img1,0.7,img2,0.2,0)
cv2.imshow('Image1',img1)
cv2.imshow('Image2',img2)
cv2.imshow('dst',dst)
cv2.imwrite("blend_image.jpg",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
