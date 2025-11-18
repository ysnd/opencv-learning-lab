import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('/home/wray/opencv/images/latest.png')
cv.imshow('tes', img)

blank=np.zeros(img.shape[:2], dtype='uint8')

#convert image warna
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)


mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask', masked)

#Grayscale histogram
#gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])


#plt.plot(gray_hist)
#plt.xlim([0,256])
#plt.show()

#color histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('n of pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
	hist=cv.calcHist([img], [i], mask, [256], [0,256])
	plt.plot(hist, color=col)
	plt.xlim([0,256])
plt.show()
cv.waitKey(0)	

