import numpy as np
import cv2 as cv

im = cv.imread('square.png')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
    print("SHAPE")
    print(len(cv.approxPolyDP(contour, 0.01*cv.arcLength(contour,True), True)))
