import cv2 as cv

img = cv.imread('/home/wray/user/images/a.jpg')
cv.imshow('res', img)

#untuk resize piture, video, live video
def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

resized_image = rescaleFrame(img)
cv.imshow('image', resized_image)


# membaca video
capture = cv.VideoCapture('/home/wray/user/video/b.mkv')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow("video resize" , frame_resized)
   
    if cv.waitKey(20) & 0xF==ord('q'):
        break

capture.release()
cv.destryAllWindows()
