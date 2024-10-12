import cv2 as cv

img = cv.imread('/home/aarin-zach/Desktop/Codes/opencv/Assets/ocv_pics/mclaren.jpg')
cv.imshow('mclaren', img)

#gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('garimg', gray)

#blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #ksize/(3,3) gotta be odd number . it increases blur intensity
cv.imshow('Blur', blur)

#edge cascade
canny = cv.Canny(img, 125, 175) #put blur instead of img to reduce edges
cv.imshow('edge', canny)

#dilate
#cv.dilate()

#erode
#cv.erode()

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('resize', resized)

#crop
cropped = img[50:200, 200:500]
cv.imshow('crop', cropped)

cv.waitKey(0)