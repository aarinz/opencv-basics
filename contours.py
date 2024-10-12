import cv2 as cv
import numpy as np



img = cv.imread('/home/aarin-zach/Desktop/Codes/opencv/Assets/ocv_pics/lambo.jpg')
cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

#can blur to significantly reduce the contours 
#threshold
ret, thresh = cv.threshold(gray, 125, 175, cv.THRESH_BINARY)
cv.imshow('threshold', thresh)

blank = np.zeros(img.shape, dtype='uint8') #img.shape retrieves the height and width of the original image 'img'
cv.imshow('blank', blank)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST ,cv.CHAIN_APPROX_NONE)
#RETR -> specify how to retrieve contours and how to handle the hierarchy of contours.
#CHAIN -> defines how contour points are stored.    
print(f'{len(contours)} countours found')

cv.drawContours(blank, contours, -1, (0,255,0), 2)
cv.imshow('contours drawn', blank)

cv.waitKey(0)

