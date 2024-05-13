import cv2
import pytesseract

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): 
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(1)
    text= pytesseract.image_to_string(frame)
    print(text)
    if key == 27: 
        break



vc.release()
cv2.destroyWindow("preview")