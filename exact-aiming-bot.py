from pyrobot import Robot, Keys
import time
import pyautogui
import winsound

robot = Robot()
pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0.1

class Coords():
    gameField = (501, 80, 1014, 533)
    startBtn = (758, 308)

def getImage():
    box = Coords.gameField

    for x in range(1,box[2]-box[0], 2):
        for y in range(1,box[3]-box[1], 2):
            color = robot.get_pixel[x,y]
            if color[0] < 30:

                pyautogui.click(Coords.gameField[0]+x+1,Coords.gameField[1]+y)


pyautogui.click(Coords.startBtn)
time.sleep(3)
while True:
    if keyboard.is_pressed('esc'):
        winsound.Beep(1000,500)
        break
    getImage()

