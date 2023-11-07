import win32gui
import win32api
import win32con
import time
from pyautogui import *
import subprocess
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import subprocess
import pygetwindow as gw
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

def click_in_window(window_title, x, y):
    hwnd = win32gui.FindWindow(None,'Ninja Legends')
    if hwnd:
        lParam = x | (y << 16)
        win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist'))
    return process_name in progs
def open_and_position_window(window_title, move_to_second_screen=True):


    window = gw.getWindowsWithTitle(window_title)

    if window:
        window = window[0] 
        screens = gw.getAllTitles()

        if move_to_second_screen and len(screens) > 1:
            window.moveTo(3000, 500)  
            window.maximize()
        elif not move_to_second_screen:

            window.maximize()
        else:
            print("No second screen found")
    else:
        print(f"Window with title '{window_title}' not found")




def main():
    count = 0
    while True:
        if process_exists('Ninja Legends.exe'):
            print("radi")
        else:
            subprocess.Popen('E:\\Ninja Legends\\Ninja Legends.exe')
            time.sleep(1)
            open_and_position_window('Ninja Legends', move_to_second_screen=True)
            time.sleep(3)
            click_in_window('Ninja Legends', 1303, 115)
            time.sleep(1)
            click_in_window('Ninja Legends', 1100, 830)
            time.sleep(1)
            click_in_window('Ninja Legends', 895, 367)
            time.sleep(1)
            click_in_window('Ninja Legends', 1637, 881)
            time.sleep(2)
            click_in_window('Ninja Legends', 1445, 155)
            time.sleep(1)
            click_in_window('Ninja Legends', 1625, 230)
            time.sleep(1)
            click_in_window('Ninja Legends', 1445, 155)
            time.sleep(1)
            print("sta radim ovde")
        click_in_window('Ninja Legends', 96, 426)
        print("1")
        time.sleep(2)
        click_in_window('Ninja Legends', 333, 145)
        print("2")
        time.sleep(2)
        
        if pyautogui.locateOnScreen('screenshot1.png') is None:
            print("ima srca")
            click_in_window('Ninja Legends', 1725, 149)
            time.sleep(5)
            click_in_window('Ninja Legends', 392, 818)
            time.sleep(5)
            click_in_window('Ninja Legends', 1139, 557)
            print('clear')
            time.sleep(2)
            click_in_window('Ninja Legends', 1545, 600)
            time.sleep(2)
            click_in_window('Ninja Legends', 1745, 890)
            print('inv')
            time.sleep(2)
            click_in_window('Ninja Legends', 1116, 590)
            print('ok')
            time.sleep(2)
            click_in_window('Ninja Legends', 1349, 341)
            print('iinv')
            time.sleep(2)
            click_in_window('Ninja Legends', 1362, 884)
            print('ok')
            time.sleep(2)
            click_in_window('Ninja Legends', 1349, 341)
            print('Kraj invajtovanja')
            time.sleep(2)
            click_in_window('Ninja Legends', 1832, 563)
            time.sleep(2)
            print('close')
            click_in_window('Ninja Legends', 96, 426)
            time.sleep(2)
            click_in_window('Ninja Legends', 333, 145)
            time.sleep(2)
            click_in_window('Ninja Legends', 1443, 545)
            time.sleep(2)
            click_in_window('Ninja Legends', 1020, 903)
            time.sleep(2)
            print(count)
            
            while pyautogui.locateOnScreen('claim1.png', confidence=0.8, grayscale=True) is None:
                click_in_window('Ninja Legends', 945, 711)
                click_in_window('Ninja Legends', 1029, 711)
                print("napadam")
                time.sleep(1.5)
            print("kraj misije")
            click_in_window('Ninja Legends', 961, 803)
            count += 1
            time.sleep(3)
        else:
            print('nema srca')
            click_in_window('Ninja Legends', 1725, 149)
            time.sleep(1)
            click_in_window('Ninja Legends', 1693, 373)
            sleep(2)
            while pyautogui.locateOnScreen('klan.png') == None:
                print("ima stamine")
                time.sleep(1)
                time.sleep(1)
                click_in_window('Ninja Legends', 320, 830)
                time.sleep(2)
                click_in_window('Ninja Legends', 830, 320)
                time.sleep(2)
                click_in_window('Ninja Legends', 1609, 887)
                time.sleep(2)
                click_in_window('Ninja Legends', 1609, 887)
                time.sleep(2)
                click_in_window('Ninja Legends', 955, 655)
                time.sleep(2)
                click_in_window('Ninja Legends', 1657, 870)
                time.sleep(2)
            print("nema")
            subprocess.call(["taskkill", "/F", "/IM", "Ninja Legends.exe"])
            time.sleep(3600)

if __name__ == "__main__":
    main()
