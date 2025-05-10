import time
import random
import pyautogui



# list of romantic messages
msg_list = [
    "You're my favorite place to go when my mind searches for peace. ❤️",
    "Every love story is beautiful, but ours is my favorite. 💕",
    "I love you more than words can express. 💖",
    "You're not just my love, you're my life. ❤️",
    "Being with you is my favorite place to be. 💞",
    "You make my world brighter and my heart lighter. ☀️💕"
]

time.sleep(10) # wait for ready

for x in range(2): # set the limit
    message = random.choice(msg_list)
    pyautogui.write(message)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)