#!/usr/bin/env python3

"""
Author: Noah Taejoon Kim
Created on Jun. 05. 2023

Mouse is automatically moving once it is activated
Keyboard strokes can start and quit the movement.

key s: start
key p: pause
key q: quit
"""

from pynput import keyboard
import pyautogui
import threading
from threading import Event
import random


class MoveMouse:

    def __init__(self):
        self.dis_size = pyautogui.size()
        print("Display size: " + str(self.dis_size))

        self.event = Event()
        self.t1 = threading.Thread(target = self.move_mouse, args = (self.event, ))
        self.t1.start()

        self.cmd = "'s'"
        self.paused = False

        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release
        ) as self.listener:
            self.listener.join()

        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )

        self.listener.start()


    def move_mouse(self, event):
        while True:
            x = random.randint(0, self.dis_size[0])
            y = random.randint(0, self.dis_size[1])

            print(f"coordinates: {x}, {y}")

            pyautogui.moveTo(x, y, duration = 1)

            if self.paused:
                event.clear()
                event.wait()

            if self.cmd == "q":
                break


    def on_press(self, key):
        try:
            pass

        except:
            print("not a keyboard")

    def on_release(self, key):
        try:
            if str(key) == "'q'":
                print("Quit")
                self.cmd = "q"
                self.event.clear()
                self.event.set()

                return False

            if str(key) == "'p'":
                print("Paused")
                self.paused = True

            elif str(key) == "'s'":
                print("Started")
                self.paused = False

                self.event.clear()
                self.event.set()

        except:
            print(key, type(key))
            print("Error occurred")


if __name__ == "__main__":
    mm = MoveMouse()







