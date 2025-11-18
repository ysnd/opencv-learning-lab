import cv2
import cv2.aruco as aruco
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Tidak dapat membuka webcam")
    exit()

camera_matrix = np.array([[800,   0, 320],
                          [  0, 800, 240],
                          [  0,   0,   1]], dtype=np.float32)
dist_coeffs = np.zeros((5, 1))  

aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()
marker_length = 0.05  # Ukuran fisik marker dalam meter (misalnya 5 cm)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal membaca frame dari webcam")
        break

    # Deteksi marker ArUco
    corners, ids, rejected = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    
    if ids is not None:
        # Gambar marker yang terdeteksi
        aruco.drawDetectedMarkers(frame, corners, ids)
        
        # Estimasi pose marker
        rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, marker_length, camera_matrix, dist_coeffs)
        
        for i in range(len(ids)):
            rvec, tvec = rvecs[i], tvecs[i]
            # Gambar axis menggunakan cv2.drawFrameAxes
            cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, rvec, tvec, marker_length * 0.5, 2)
            
            # Tampilkan informasi pose (x, y, z) pada marker
            x, y, z = tvec[0]
            text = f"X: {x:.2f}m, Y: {y:.2f}m, Z: {z:.2f}m"
            # Menempatkan teks di sudut marker (menggunakan koordinat sudut pertama)
            pos = (int(corners[i][0][0][0]), int(corners[i][0][0][1]))
            cv2.putText(frame, text, pos, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("ArUco Pose Estimation", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Keluar dengan tombol ESC
        break

cap.release()
cv2.destroyAllWindows()

