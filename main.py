from pyautogui import *
import subprocess
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import subprocess
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist'))
    if process_name in progs:
        return True
    else:
        return False
count=0
sleep(3)
while 1:
    if process_exists('Ninja Legends.exe'):
        print("radi")
    else:
        subprocess.Popen('E:\\Ninja Legends\\Ninja Legends.exe')
        sleep(5)
        click(1303,115)
        sleep(1)
        click(1100,830)
        sleep(1)
        click(895,367)
        sleep(1)
        click(1637,881)
        sleep(2)
        click(1445,155)
        sleep(1)
        click(1625,230)
        sleep(1)
        click(1445,155)
        sleep(1)
        print("sta radim ovde")
    click(96,426)
    print("1")
    sleep(2)
    click(333,145)
    print("2")
    sleep(2)
    if pyautogui.locateOnScreen('screenshot1.png')==None:
        print("ima srca")
        click(1725,149)
        sleep(5)
        click(392,818)
        sleep(5)
        click(1125,591) 
        sleep(1)
        click(1545,890)
        sleep(1)
        click(1745,890)
        sleep(1)
        click(1116,590)
        sleep(1)
        click(1349,341)
        sleep(1)
        click(1362,884)
        sleep(1)
        click(1349,341)
        sleep(1)
        click(1832,600)
        sleep(1)
        click(96,426)
        sleep(2)
        click(333,145)
        sleep(2)
        click(1443,545) 
        sleep(1)
        click(947,927) 
        sleep(1)
        print(count)
        while pyautogui.locateOnScreen('claim1.png',confidence=0.8,grayscale=True)== None:
            click(945,711)
            click(1029,711)
            print("napadam")
            sleep(1.5)
        print("kraj misije")
        click(961,803)
        count=count+1
        sleep(3)
    else:
        print('nema srca')
        click(1855,89)
        click(1855,89)
        subprocess.call(["taskkill","/F","/IM","Ninja Legends.exe"])
        sleep(3600)
        continue
    """
            if pyautogui.locateOnScreen('lvlup.png')!= None:
                click(1879,799)
                print("Level up")
                sleep(3)
                count=count+1
            else:
                count=count+1
                print("agane")
            

    subprocess.call(["taskkill","/F","/IM","Ninja Legends.exe"])
    """
