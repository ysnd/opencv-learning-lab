import cv2
import mediapipe as mp
import serial
import time


ser = serial.Serial('COM10', 9600)  
time.sleep(2)  #

# MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # Konversi BGR ke RGB untuk MediaPipe
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Konversi RGB ke BGR kembali untuk ditampilkan di OpenCV
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Gambar landmark tangan di atas video
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Ambil posisi landmark jempol (landmark ke-4 adalah ujung jempol)
            thumb_tip = hand_landmarks.landmark[4]  # Landmark 4 adalah ujung jempol
            
            # Skalakan posisi x jempol ke dalam rentang 0-100 untuk dikirim ke Arduino
            thumb_x = int(thumb_tip.x * 100)
            
            # Kirim posisi jempol (x-axis) ke Arduino
            ser.write(f"{thumb_x}\n".encode())
            
            # Tampilkan data yang dikirim ke console
            print(f"Mengirim nilai X Jempol: {thumb_x}")

    # Tampilkan frame video dengan landmark
    cv2.imshow('MediaPipe Hands', image)

    if cv2.waitKey(5) & 0xFF == 27:  # Tekan ESC untuk keluar
        break

# Bersihkan semua resource
cap.release()
ser.close()
cv2.destroyAllWindows()
