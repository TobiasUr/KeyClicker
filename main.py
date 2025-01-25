import keyboard
import threading
import time
import tkinter as tk


clicking = False

def press_key(key):
    keyboard.press_and_release(key)

def main(keys, time_interval):
    global clicking
    while True:
        if clicking:
            for key in keys:
                press_key(key)
                time.sleep(time_interval)
        else:
            time.sleep(0.1)

def start():
    global clicking
    keys = input("Enter the keys you want to press (comma-separated): ").split(',')
    time_interval = float(input("Enter the time interval: "))
    t1 = threading.Thread(target=main, args=(keys, time_interval))
    t1.start()
    while True:
        if keyboard.is_pressed("F12"):
            clicking = not clicking
            time.sleep(0.5)




if __name__ == "__main__":
    start()