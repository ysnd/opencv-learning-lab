import cv2
import cv2.aruco as aruco
import numpy as np

cap = cv2.VideoCapture(0)

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()


camera_matrix = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])
dist_coeffs = np.zeros((5,1)) 

while True:
    ret, frame = cap.read()
    if not ret:
        break

    corners, ids, _ = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    
    if ids is not None:
        # Estimasi pose untuk setiap marker
        rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, 0.1, camera_matrix, dist_coeffs)
        
        for i in range(len(ids)):
            # Gambar sumbu pada marker
            cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, rvecs[i], tvecs[i], 0.1)
            
            # Tampilkan posisi (x, y, z)
            x, y, z = tvecs[i][0]
            print(f"Marker ID {ids[i][0]}: Position (x, y, z) = ({x:.2f}, {y:.2f}, {z:.2f})")

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
