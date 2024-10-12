import cv2 as cv

img = cv.imread('/home/aarin-zach/Desktop/Codes/opencv/Assets/ocv_pics/chico.jpg')
cv.imshow('Guy', img)

# img = cv.imread('/home/aarin-zach/Desktop/Codes/opencv/Assets/ocv_pics/group 2.jpg')
# cv.imshow('group', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('/home/aarin-zach/Desktop/Codes/opencv/Faces/haar_face.xml')

faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
print(f'Number  of faces found = {len(faces)}')

for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('detected face', img)

cv.waitKey(0)