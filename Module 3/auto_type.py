import pyautogui
from time import sleep
sleep(6)
for i in range(0,3):
    pyautogui.write('I love you, Nilu',interval=.025)
    pyautogui.press('enter')

