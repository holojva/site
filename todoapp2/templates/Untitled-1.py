import pyautogui
import time
time.sleep(5)
for i in range(10000) :
    im2 = pyautogui.screenshot(region=(0, 80, 500, 580))
    im2.save("C:/Users/dadoc/", "JPEG")
    for i in range(11):
        pyautogui.press("down")