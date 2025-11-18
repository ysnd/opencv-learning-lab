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

# Parameter ArUco
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()
# Tentukan ukuran marker secara nyata (misalnya 0.05 meter = 5 cm)
marker_length = 0.05

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
        
        # Estimasi pose untuk setiap marker
        # rvecs: rotation vectors, tvecs: translation vectors (dalam satuan marker_length)
        rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, marker_length, camera_matrix, dist_coeffs)
        
        # Iterasi untuk setiap marker
        for i in range(len(ids)):
            rvec, tvec = rvecs[i], tvecs[i]
            
            # Gambar axis (sumbu) pada marker (axis length disesuaikan, misalnya setengah marker_length)
            aruco.drawAxis(frame, camera_matrix, dist_coeffs, rvec, tvec, marker_length * 0.5)
            
            # Tampilkan informasi pose (x, y, z) pada marker
            # tvec merupakan array berukuran 1x3, ambil nilainya untuk ditampilkan
            x, y, z = tvec[0]
            text = f"X: {x:.2f}m, Y: {y:.2f}m, Z: {z:.2f}m"
            
            # Tempatkan teks di posisi sudut marker pertama (konversi ke integer)
            corner = corners[i][0][0]  # mengambil sudut pertama dari marker ke-i
            pos = (int(corner[0]), int(corner[1]))
            cv2.putText(frame, text, pos, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Tampilkan frame hasil deteksi dan estimasi pose
    cv2.imshow("ArUco Pose Estimation", frame)
    
    # Keluar jika tombol esc ditekan
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

