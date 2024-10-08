import cv2 as cv

img = cv.imread('/home/aarin-zach/Desktop/Codes/opencv/ocv_pics/lambo.jpg')
cv.imshow('Car', img) 

def Rescale(frame, scale=0.4):
    #works for imgs, vids, live vids
    width = int(frame.shape[1] * scale) #1 is width
    height = int(frame.shape[0] * scale) #0 is height
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# def changeRes(width,height):
#     #works for live vids only
#     capture.set(3,width)
#     capture.set(4,height)


resized_img = Rescale(img)
cv.imshow('resized img', resized_img)

capture = cv.VideoCapture('opencv/ocv_vid/carvid1.mp4') 
while True:
    isTrue, frame = capture.read()

    frame_resized = Rescale(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('vid resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('e'): 
        break

capture.release()
cv.destroyAllWindows()