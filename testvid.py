import cv2 as cv

cap = cv.VideoCapture(0)  # 0 untuk webcam
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
