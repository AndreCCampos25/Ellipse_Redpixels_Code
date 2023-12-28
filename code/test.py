import cv2
import numpy as np

def get_orientation(contour):
    (x, y), (MA, ma), angle = cv2.fitEllipse(contour)
    if MA > ma:
        return angle
    else:
        return angle + 90

image=1
    
img = cv2.imread("../data/Zoom/{}.jpg".format(image))
img_suave = cv2.GaussianBlur(img, (5, 5), 0)
img_hsv = cv2.cvtColor(img_suave, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 200, 50])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

lower_red = np.array([170, 200, 50])
upper_red = np.array([180, 255, 255])
mask2 = cv2.inRange(img_hsv, lower_red, upper_red)

mask = cv2.bitwise_or(mask1, mask2)
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

num_pixels = cv2.countNonZero(opening)
print("Number of Red Pixels: ",num_pixels)

angle_array=[]
angle=None
contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_contours = img.copy()
for contour in contours:
	area = cv2.contourArea(contour)
#	print(area)
	if area < 100 or area > 10000:
		continue
	ellipse = cv2.fitEllipse(contour)
	cv2.ellipse(img_contours, ellipse, (0,255,0), 2)
	angle = get_orientation(contour)
print('Ellipse Inclination Angle: ', angle)
angle_array.append(angle)

cv2.imwrite("../data/Ellipse/{}_ellipse.jpg".format(image), img_contours)