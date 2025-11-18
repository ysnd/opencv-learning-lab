import cv2
print("Versi OpenCV:", cv2.__version__)

# Cek apakah modul aruco tersedia
if 'aruco' in dir(cv2):
    print("ArUco support: Tersedia")
else:
    print("ArUco support: Tidak tersedia (install opencv-contrib-python)")
