import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Audrey', 'Dani', 'Eimi', 'Johny', 'Maria']

# Muat model pengenalan wajah yang sudah dilatih
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# Baca gambar yang akan dikenali
img = cv.imread(r'/home/wray/opencv/images/6.jpg')

# Ubah gambar ke grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Deteksi wajah dalam gambar
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

# Loop melalui semua wajah yang terdeteksi
for (x, y, w, h) in faces_rect:
    # Ambil ROI (Region of Interest) wajah
    faces_roi = gray[y:y+h, x:x+w]
    
    # Prediksi label dan confidence
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    
    # Tampilkan label dan kotak di sekitar wajah
    cv.putText(img, str(people[label]), (x, y-10), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

# Tampilkan gambar dengan hasil deteksi dan pengenalan
cv.imshow('Detected Face', img)
cv.waitKey(0)
