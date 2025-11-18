import cv2 as cv
import time
prev_time = 0

cap = cv.VideoCapture(0)  # 0 untuk webcam
if not cap.isOpened():
    print('Elor: Webcam te bisa di buka kehed!')
    exit()

face_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        print('Elor: Frame hnte kabaca!')
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255,0), 2)
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    cv.putText(frame, f"FPS: {int(fps)}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv.imshow('Face Detection', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

