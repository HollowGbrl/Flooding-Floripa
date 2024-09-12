import psutil
import time
import pyautogui


def checkapp():
#Get a list of process names
    highest_cpu_usage = 0
    print('comecei a verificar o maior uso da cpu as:', time.ctime())
# Get CPU usage for each process
    for proc in psutil.process_iter():
        if proc.cpu_percent(interval=1) > highest_cpu_usage:
            highest_cpu_usage = proc.cpu_percent(interval=1)
            highest_cpu_usage_pid = proc.pid
            procalto=proc
    print('o proc alto é:', procalto)
    while procalto in psutil.process_iter() and procalto.cpu_percent(interval=1) > 100:
        print('dei uma olhadinha no processamento as:', time.ctime())
        time.sleep(150)
    print('hora de salvar')

#Move the mouse to a certain location on the taskbar
# Open the deltashell.gui app
checkapp()
pyautogui.moveTo(1020, 1030, duration=0.5)
pyautogui.leftClick()
time.sleep(10)
pyautogui.hotkey('ctrl', 's')


