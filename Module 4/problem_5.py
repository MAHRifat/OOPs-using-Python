import pyautogui
from time import sleep

N =int(input())
sleep(6)
for i in range(N):
    for j in range(i+1):
        pyautogui.drawRect('#',interval=0.025)
    print()