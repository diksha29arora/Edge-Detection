import cv2 as cv
import numpy as np

img = cv.imread('test.jpg')

cv.imwrite('RGB.png',img)
img = cv.cvtColor(img , cv.COLOR_BGR2RGB)

cv.imwrite('BGR.png',img)
img = cv.cvtColor(img , cv.COLOR_RGB2GRAY)

cv.imwrite('Gray.png',img)

img = cv.Canny(img , threshold1 = 200, threshold2 = 300)
cv.imwrite('Edge.png',img)
