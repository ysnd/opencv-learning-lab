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
dist_coeffs = np.zeros((0, 0)) 

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters()
marker_length = 0.05  #5 cm dalam meter

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
            # Gambar axis
            cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, rvec, tvec, marker_length * 0.5, 2)
            
            # Ambil posisi (x, y, z)
            x, y, z = tvec[0]
            
            # Tampilkan informasi pose di sudut kiri atas
            text = f"ID {ids[i][0]} | X: {x:.2f}m, Y: {y:.2f}m, Z: {z:.2f}m"
            cv2.putText(frame, text, (10, 30 + i*30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("ArUco Pose Estimation", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Keluar dengan tombol ESC
        break

cap.release()
cv2.destroyAllWindows()
