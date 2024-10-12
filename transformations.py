import cv2 as cv
import numpy as np

img = cv.imread('/home/aarin-zach/Desktop/Codes/opencv/Assets/ocv_pics/lambo.jpg')
cv.imshow('Car', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])#1 is width. 0 is height
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, 100, -100)
cv.imshow('Translated', translated)

#rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

#flipping
flip = cv.flip(img, 0)# 0 vertically, 1 horizontally, -1 both vert nd hori
cv.imshow('flip', flip)


cv.waitKey(0)