import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('home1.JPG')
# Step1 转化为HSV
hue_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Step2. 用颜色分割图像
blue_low_range = np.array([100, 43, 46])
blue_high_range = np.array([124, 255, 255])

orange_low_range = np.array([15, 43, 46])
orange_high_range = np.array([25, 200, 200])

red_low_range = np.array([0, 43, 46])
red_high_range = np.array([5, 255, 255])

blue = cv2.inRange(hue_image, blue_low_range, blue_high_range)
orange = cv2.inRange(hue_image, orange_low_range, orange_high_range)
red = cv2.inRange(hue_image, red_low_range, red_high_range)
# step3 形态学变换：膨胀
dilated = cv2.dilate(blue, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=4)
dilated2 = cv2.dilate(orange, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=4)
dilated3 = cv2.dilate(red, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=4)
# Step4. Hough Circle
circles = cv2.HoughCircles(dilated, cv2.HOUGH_GRADIENT, 1, 100, param1=15, param2=7, minRadius=10, maxRadius=200)
circles2 = cv2.HoughCircles(dilated2, cv2.HOUGH_GRADIENT, 1, 150, param1=15, param2=15, minRadius=10, maxRadius=200)
circles3 = cv2.HoughCircles(dilated3, cv2.HOUGH_GRADIENT, 1, 150, param1=15, param2=20, minRadius=10, maxRadius=200)

# Step5. 绘制
print(len(circles[0]))
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 3)
    # draw the center of the circle
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    # show the coordinates of the circle
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = str(i[0])+','+str(i[1])+','+str(i[2])
    cv2.putText(img,text,(i[0], i[1]),font,1.2,(255,255,255),2)
print(len(circles2[0]))
circles2 = np.uint16(np.around(circles2))
for i in circles2[0, :]:
    # draw the outer circle
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 3)
    # draw the center of the circle
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    # show the coordinates of the circle
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = str(i[0])+','+str(i[1])+','+str(i[2])
    cv2.putText(img,text,(i[0], i[1]),font,1.2,(255,255,255),2)

print(len(circles3[0]))
circles3 = np.uint16(np.around(circles3))
for i in circles3[0, :]:
    # draw the outer circle
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 3)
    # draw the center of the circle
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    # show the coordinates of the circle
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = str(i[0])+','+str(i[1])+','+str(i[2])
    cv2.putText(img,text,(i[0], i[1]),font,1.2,(255,255,255),2)

cv2.imshow('detected circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

