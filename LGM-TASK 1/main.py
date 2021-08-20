import cv2
image = cv2.imread("test.jpg") #Reading the image
cv2.imshow("result", image) #original image
cv2.waitKey(0)
#Converting Image to gray scale
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray-scale",gray) #gray scale image
cv2.waitKey(0)
inverted= 255 - gray
cv2.imshow("Inverted", inverted)
cv2.waitKey(0)
#Blurring the image using Gaussian Blur
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)
invertblurred = 255 - blurred
#Division of the images
pencil = cv2.divide(gray, invertblurred, scale=256.0)
cv2.imshow("Sketch", pencil)
cv2.waitKey(0)
