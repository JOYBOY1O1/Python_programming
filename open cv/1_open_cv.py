import cv2 as c

cap = c.VideoCapture(2)
cap.set(4,480)
cap.set(3,360)
cap.set(10,100)
faceCas = c.CascadeClassifier("Res/some.xml")

img = c.imread("Res/kawai.jpg")
imgGray = c.cvtColor(img,c.COLOR_BGR2GRAY)
# imgBlur = c.GaussianBlur(imgGray,(7,7),0)
faces = faceCas.detectMultiScale(imgGray,1.1,4)

for(x,y,w,h) in faces:
    c.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
c.imshow("Result",img)
#
# c.imshow("Blur",imgBlur)
# c.imshow("Gray",imgGray)


c.waitKey(0)
# while True:
#     success,img = cap.read()
#     c.imshow("Video",img)
#     if c.waitKey(1) & 0xFF ==ord('q'):
#         break