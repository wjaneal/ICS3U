import cv2
# initialize the camera
cam = cv2.VideoCapture(-1)   # 0 -> index of camera
s, img = cam.read()
print s
print img
if s:    # frame captured without any errors
    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("cam-test",img)
    waitKey(0)
    destroyWindow("cam-test")
    imwrite("filename.jpg",img) #save image
else:
	print "Error"
