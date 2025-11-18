import cv2 as cv
import numpy as np

img = cv.imread('/home/wray/opencv/images/4.jpg')
if img is None:
    print('Error Gambar Teukabaca')
    exit()

#ImageManipulation
rz = cv.resize(img, None, fx=0.8, fy=0.8)
gray = cv.cvtColor(rz, cv.COLOR_BGR2GRAY)
(h, w)= img.shape[:2]
center = (w //2, h// 2)
mtrx = cv.getRotationMatrix2D(center, 45,1.0)
rttd = cv.warpAffine(img, mtrx, (w, h))
croped= img[50:300, 100:400]
#Edge Detection
#canny = cv.Canny(gray, 100, 200)#threshold1,2
#GaussianBlur
blur=cv.GaussianBlur(img, (5, 5), 0)
gry=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gry, 50, 150)#threshold1,2
#Thresholding
_, thres = cv.threshold(gray, 127, 255, cv.THRESH_BINARY) 
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

lines = cv.HoughLinesP(
    canny,          # Gambar tepi (edge)
    1,              # Resolusi rho (1 pixel)
    np.pi / 180,    # Resolusi theta (1 derajat dalam radian)
    threshold=50,   # Minimal vote untuk dianggap sebagai garis
    minLineLength=50,  # Panjang minimal garis (pixel)
    maxLineGap=10     # Jarak maksimal antar segmen garis yang dihubungkan
)

# Gambar garis pada gambar asli
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Warna hijau, ketebalan 2

#countours
contours, _ = cv.findContours(adaptive_thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (0, 255, 0), 3)

cv.imshow('Gambar', img)
cv.imshow('gambar Resize', rz)
cv.imshow('Gambar HitamPutih', gray)
cv.imshow('Gambar Rotet', rttd)
cv.imshow('Gambar Crop', croped)
cv.imshow('Gambar Canny', canny)
cv.imshow('Gambar Blur', blur)
cv.imshow('Gambar Thresh', thres)
cv.imshow('Gambar AdaptiveThresh', adaptive_thresh)
cv.imshow('Hough Lines', canny)
cv.imshow('Contours', img)

cv.waitKey(0)
cv.destroyAllWindows()
