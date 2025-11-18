import cv2
import cv2.aruco as aruco

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Tidak dapat membuka webcam")
    exit()


aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal membaca frame dari webcam")
        break

    # Deteksi marker pada frame
    corners, ids, rejected = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    
    # Jika ada marker yang terdeteksi, gambar batas dan ID-nya pada frame
    if ids is not None:
        frame = aruco.drawDetectedMarkers(frame, corners, ids)

    cv2.imshow("ArUco Detection", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

