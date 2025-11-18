import cv2
import cv2.aruco as aruco
import numpy as np

marker_id = 0            # ID marker
side_pixels = 200        # Ukuran marker: 200 x 200 piksel
save_path = 'marker0.png'

aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)

marker_image = np.zeros((side_pixels, side_pixels), dtype=np.uint8)

marker_image = aruco.drawMarker(aruco_dict, marker_id, side_pixels, marker_image, 1)

cv2.imwrite(save_path, marker_image)
print(f"Marker ArUco dengan ID {marker_id} telah disimpan ke '{save_path}'")

cv2.imshow('ArUco Marker', marker_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

