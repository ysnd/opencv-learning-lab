import cv2 as cv

# file jang video

capture = cv.VideoCapture('/home/user/opencv/video/a.mp4')

while True:
    isTrue, frame = capture.read()
   
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()
    
