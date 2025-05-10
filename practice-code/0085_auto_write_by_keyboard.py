# pip install pyautogui

import pyautogui


pyautogui.click(100, 100)
pyautogui.typewrite('hi, this is me?')

x, y = pyautogui.position()
print(x, y)