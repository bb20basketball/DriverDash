import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread("testBird.png", 1) #cv.IMREAD_COLOR


image = np.zeros((700, 700, 3), np.uint8)
image2 = np.zeros((700, 700, 3), np.uint8) 
src = np.array([[0,200],[480,200],[480,360],[0,360]],np.float32)
dst = np.array([[0,0],[480,0],[300,200],[180,200]],np.float32)
##########################Pushing   ^^ Down to below 200 gives the weird image

M = cv.getPerspectiveTransform(src, dst)
warp = cv.warpPerspective(img1.copy(), M, (480, 360))



two = warp.copy()
two = cv.resize(two,(0,0), fx=2, fy=2)

three = two.copy()
four = two.copy()

image2[:warp.shape[0], 15:warp.shape[1]+15]= warp
twoR = cv.getRotationMatrix2D((two.shape[1]/2,two.shape[0]/2),90,.5)
twoD = cv.warpAffine(two,twoR,(two.shape[1],two.shape[0]))

threeR = cv.getRotationMatrix2D((three.shape[1]/2,three.shape[0]/2),180,.5)
threeD = cv.warpAffine(three,threeR,(three.shape[1],three.shape[0]))

fourR = cv.getRotationMatrix2D((four.shape[1]/2,four.shape[0]/2),270,.5)
fourD = cv.warpAffine(four,fourR,(four.shape[1],four.shape[0]))



twoD = twoD[100:600, 310:500]
threeD = threeD[]
fourD = fourD[]
image[0:twoD.shape[0]+0, 0:twoD.shape[1]+0]= twoD


ora = cv.add(image, image2)

cv.imwrite('blank.png', ora)

