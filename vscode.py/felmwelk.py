import cv2
import os 
import pytesseract
webcam=cv2.VideoCapture(0)

while True:
    rd , frame= webcam.read()
    cv2.imshow("secret",frame)
    key=cv2.waitKey(1)
    
    text= pytesseract.image_to_string(frame)
    print(text)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows("secret")