import cv2
import cv2.aruco as aruco

image = cv2.imread("/home/user/opencv/images/1.png")  # Ganti dengan nama file gambarmu

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
aruco_params = aruco.DetectorParameters()

detector = aruco.ArucoDetector(aruco_dict, aruco_params)
corners, ids, _ = detector.detectMarkers(image)


if ids is not None:
    aruco.drawDetectedMarkers(image, corners, ids)

    for i in range(len(ids)):
        corner = corners[i][0]
        x, y = int(corner[0][0]), int(corner[0][1])  # Koordinat atas kiri marker
        cv2.putText(image, f"ID: {ids[i][0]}", (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow("ArUco Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

