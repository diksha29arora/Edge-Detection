import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
	_,img = cap.read()
	img = cv.cvtColor(img , cv.COLOR_BGR2RGB)
	img = cv.cvtColor(img , cv.COLOR_RGB2GRAY)

	img = cv.Canny(img , threshold1 = 50, threshold2 = 100)
	cv.imshow('Edge',img)
	cv.waitKey(30)

	key = cv.waitKey()
	
	if(key == 27):
		cv.destroyAllWindows()
		break
