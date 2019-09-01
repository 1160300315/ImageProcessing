import cv2
# 坐标原点返回0，蓝色返回1，黄色返回2
def classify_curling(image, local_x, local_y):
    points = [(local_x + 5, local_y), (local_x + 5, local_y - 5),
              (local_x, local_y - 5), (local_x - 5, local_y - 5),
              (local_x - 5, local_y), (local_x - 5, local_y + 5),
              (local_x, local_y + 5), (local_x + 5, local_y + 5)]
    count = 0
    for point in points:
        if image[point[1], point[0], 2] < 100:
            count = count + 1
        else:
            count = count - 1
    if count > 4:
        return 1  # 蓝色
    elif count < -4:
        return 2  # 黄色
    else:
        return 0


# 载入图片
# cap = cv2.VideoCapture("http://192.168.0.33:8080/?action=stream")
# ret, img = cap.read()
# cv2.imshow("img", img)
# cv2.waitKey(0)
img = cv2.imread("192.168.0.33.jpg")

# def curing_image(img):
# 降噪（模糊处理用来减少瑕疵点）
blur_image = cv2.blur(img, (5, 5))
# 灰度化,就是去色（类似老式照片）
gray = cv2.cvtColor(blur_image, cv2.COLOR_BGR2GRAY)

# param1的具体实现，用于边缘检测
canny = cv2.Canny(img, 40, 80)

# 霍夫变换圆检测
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=20,
                            minRadius=10, maxRadius=20)

# 输出检测到圆的个数
# print(len(circles[0]))

# print('-------------我是条分割线-----------------')
origin = None
blue_balls = []
yellow_balls = []
# 根据检测到圆的信息，画出每一个圆
for circle in circles[0]:
    # 坐标行列(就是圆心)
    x = int(circle[0])
    y = int(circle[1])
    # 半径
    r = circle[2]
    if classify_curling(img, x, y) == 0:
        origin = (x, y, r)
    elif classify_curling(img, x, y) == 1:
        blue_balls.append((x, y, r))
    else:
        yellow_balls.append((x, y, r))
print(origin)
print(blue_balls)
print(yellow_balls)
list = [blue_balls, yellow_balls, origin]
# return list
