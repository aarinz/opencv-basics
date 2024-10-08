import cv2 as cv
import numpy as np

Blank = np.zeros((500,500, 3), dtype='uint8') #dtype uint8 is of a img
cv.imshow('Blank_img', Blank) #displays blankimg

#paint the img a certain color
Blank[:] = 0,100,0
cv.imshow('green', Blank)

#rectangle
cv.rectangle(Blank, (0,0), (100,100), (0,255,0), thickness=2) #if filled box put thickness=cv.FILLED
cv.imshow('rect', Blank) 

#circle
#cv.circle()

#line
cv.line(Blank, (0,0), (100,100), (0,255,0), thickness=5) 
cv.imshow('Line', Blank) 

#text
cv.putText(Blank, 'YOLO', (255,255), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (0,255,0), 2 )
cv.imshow('Text', Blank)

cv.waitKey(0)