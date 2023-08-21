from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

time.sleep(5)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(491,205)[0] == 74:
        click(491,205)
    if pyautogui.pixel(616,205)[0] == 74:
        click(616,205)
    if pyautogui.pixel(733,205)[0] == 74:
        click(733,205)
    if pyautogui.pixel(850,205)[0] == 74:
        click(850,205)
    if pyautogui.pixel(491,325)[0] == 74:
        click(491,325)
    if pyautogui.pixel(616,325)[0] == 74:
        click(616,325)
    if pyautogui.pixel(733,325)[0] == 74:
        click(733,325)
    if pyautogui.pixel(850,325)[0] == 74:
        click(850,325)
    if pyautogui.pixel(491,444)[0] == 74:
        click(491,444)
    if pyautogui.pixel(616,444)[0] == 74:
        click(616,444)
    if pyautogui.pixel(733,444)[0] == 74:
        click(733,444)
    if pyautogui.pixel(850,444)[0] == 74:
        click(850,444)
    if pyautogui.pixel(491,560)[0] == 74:
        click(491,560)
    if pyautogui.pixel(616,560)[0] == 74:
        click(616,560)
    if pyautogui.pixel(733,560)[0] == 74:
        click(733,560)
    if pyautogui.pixel(850,560)[0] == 74:
        click(850,560)
    