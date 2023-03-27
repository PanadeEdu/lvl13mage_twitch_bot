import pyautogui
import random

class MechabellumMacro():

    def buy_shield():
        x_orig, y_orig = pyautogui.position()
        # buy a shield
        x = 2480
        y = 1210
        pyautogui.click(x, y)
        pyautogui.moveTo(x_orig, y_orig)

    def buy_rocket():
        x_orig, y_orig = pyautogui.position()
        # buy a shield
        x = 2480
        y = 1210
        pyautogui.click(x, y)
        pyautogui.moveTo(x_orig, y_orig)

    def buy_unit(slot: int):
        buy_slots = [
            (2310, 1200),
            (2310, 1460),
            (2160, 1200),
            (2160, 1460),
            (2010, 1200),
            (2010, 1460),
            (1850, 1200),
            (1850, 1460),
            (1710, 1200),
            (1710, 1460),
            (1550, 1200),
            (1550, 1460),
            (1400, 1200),
            (1400, 1460)
        ]
        x_orig, y_orig = pyautogui.position()
        # buy a shield on slot
        x = buy_slots[slot-1][0]
        y = buy_slots[slot-1][1]
        pyautogui.click(x, y)
        pyautogui.moveTo(x_orig, y_orig)

    def click_random():
        x_orig, y_orig = pyautogui.position()
        # randomized mouse movement each time this function is called
        x = random.randrange(250, 250)
        y = random.randrange(2500, 900)
        pyautogui.click(x, y)
        pyautogui.moveTo(x_orig, y_orig)