import cv2
import cv2.aruco as aruco

cap = cv2.VideoCapture(0, cv2.CAP_V4L2) 

if not cap.isOpened():
    print("[ERROR] Kamera tidak bisa diakses!")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[WARN] Frame tidak terbaca")
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        
        if ids is not None:
            aruco.drawDetectedMarkers(frame, corners, ids)
        
        cv2.imshow('ArUco Fix', frame)
        if cv2.waitKey(1) == ord('q'):
            break

except Exception as e:
    print(f"[CRASH] Error: {str(e)}")

finally:
    cap.release()
    cv2.destroyAllWindows()
