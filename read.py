import cv2 as cv


# #images
# img = cv.imread('/home/aarin-zach/Desktop/Codes/opencv/ocv_pics/lambo.jpg')
# cv.imshow('Car', img) #'win name', variable

# cv.waitKey(0) 


#vidoes
capture = cv.VideoCapture('opencv/ocv_vid/carvid1.mp4') # inside bracket write 0 if webcam or 1 or 2 if other cams and path is vid

while True:
    isTrue, frame = capture.read()#reads frame by frame
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('e'): #press e to get out of the vidloop
        break

capture.release()
cv.destroyAllWindows()

