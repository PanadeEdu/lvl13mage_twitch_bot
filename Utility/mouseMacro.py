import pyautogui
import random

class MouseMacro():

    def mouse_random():
        # randomized mouse movement each time this function is called
        x = random.randrange(-100, 100)
        y = random.randrange(-50, 50)
        speed = round(random.uniform(0.01, 1), 2)
        pyautogui.moveRel(x, y, duration=speed)
        print('mouse jitter')
        print(x, y, speed)

    def mouse_up():
        # randomized mouse movement each time this function is called
        x = 0
        y = -10
        speed = 0.10
        pyautogui.moveRel(x, y, duration=speed)

    def mouse_down():
        # randomized mouse movement each time this function is called
        x = 0
        y = 10
        speed = 0.10
        pyautogui.moveRel(x, y, duration=speed)

    def mouse_left():
        # randomized mouse movement each time this function is called
        x = -10
        y = 0
        speed = 0.10
        pyautogui.moveRel(x, y, duration=speed)
    
    def mouse_right():
        # randomized mouse movement each time this function is called
        x = 10
        y = 0
        speed = 0.10
        pyautogui.moveRel(x, y, duration=speed)