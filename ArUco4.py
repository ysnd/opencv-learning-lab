import cv2
import cv2.aruco as aruco


cap = cv2.VideoCapture(0) 

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters_create()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      
    corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    if ids is not None:  # Jika ada marker yang terdeteksi
        aruco.drawDetectedMarkers(frame, corners, ids)  # Gambar kotak & ID marker

        # Loop melalui setiap marker yang terdeteksi
        for i in range(len(ids)):
            corner = corners[i][0]  # Koordinat sudut marker
            x, y = int(corner[0][0]), int(corner[0][1])  # Ambil koordinat sudut kiri atas

            # Tampilkan ID marker di atasnya
            cv2.putText(frame, f"ID: {ids[i][0]}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.8, (0, 255, 0), 2, cv2.LINE_AA)

    # Tampilkan hasil
    cv2.imshow("ArUco Marker Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()

