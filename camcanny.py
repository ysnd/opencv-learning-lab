import cv2 as cv

cap = cv.VideoCapture(0)  # 0 untuk webcam
if not cap.isOpened():
    print('Elor: Webcam te bisa di buka kehed!')
    exir()

while True:
    ret, frame = cap.read()
    if not ret:
        print('Elor: Frame hnte kabaca!')
        break
    gr = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    sisi=cv.Canny(gr, 100, 200)
    cv.imshow('Video canny', sisi)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

