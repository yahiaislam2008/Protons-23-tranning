import pyautogui as py
import time 

message = "5alony"
count = 1

time.sleep(2)

for i in range(100):
    py.typewrite(message)
    py.press("Enter")
    count = count + 1
