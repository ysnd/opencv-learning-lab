import cv2 as cv

img = cv.imread('/home/wray/opencv/images/lady2.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayPerson', gray)

haar_cascade = cv.CascadeClassifier('/home/wray/opencv/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=6, minNeighbors=3)
print(f'Number of faces fount = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
cv.imshow('detection',img)

cv.waitKey(0)
