from pynput import keyboard
import subprocess
import sys
import os
import signal
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLineEdit, QApplication, QHBoxLayout

class xWindow(QLineEdit):
    def __init__(self):
        super().__init__()

        get_wmctrl_installed = subprocess.run(["apt", "search", "wmctrl"], capture_output=True)
        if get_wmctrl_installed:
            wmctrl_status = get_wmctrl_installed
        else:
            raise ModuleNotFoundError

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.textChanged.connect(self.text_change)
        self.space = False

        self.trigger = {keyboard.Key.ctrl_l, keyboard.Key.alt_l, keyboard.KeyCode(char='x')}
        self.execute = {keyboard.Key.enter}
        self.pressed = set()

        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()


    def text_change(self, text):
        new = ""
        validate = ""
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.x = False

        for char in text:
            if char == " " and self.space is not True and self.x is not True:
                self.space = True
                new += "x"
                self.x = True
            elif char not in numbers and char != "x":
                new += ""
            elif char == "x":
                if not self.x:
                    new += "x"
                    self.x = True
            else:
                new += char

        if "x" not in new:
            self.space = False
            self.x = False

        if new == "x":
            new = ""

        if new != text:
            cursor = self.cursorPosition()
            self.setText(new)
            self.setCursorPosition(max(cursor, len(new)))


    def get_text(self):
        resize_parameters = self.text()
        w, h = resize_parameters.split("x")
        w, h = int(w), int(h)
        if w and h:
            return w,h
        else:
            raise ValueError

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            try:
                w, h = self.get_text()
                if w and h:
                    params = f"0,0,0,{w},{h}"
                    subprocess.run(["wmctrl", "-i", "-r", self.window, "-e", params])
                    self.hide()
            except ValueError:
                self.setText("Invalid")
        elif event.key() == Qt.Key_Escape:
            self.hide()
        else:
            super().keyPressEvent(event)

    def on_press(self,key,w=None,h=None):
        try:
            self.pressed.add(key)
            if all(k in self.pressed for k in self.trigger):
                subprocess.Popen(["python", "xresize.py"])

            elif all(k in self.pressed for k in self.execute):
                try:
                    w,h = self.get_text()
                    if w and h:
                        params = f"0,0,0,{w},{h}"
                        subprocess.run(["wmctrl", "-i", "-r", self.window, "-e", params])
                except ValueError:
                    self.setText("Invalid")

        except AttributeError:
            self.pressed.add(key)
            if all(k in self.pressed for k in self.trigger):
                subprocess.Popen(["python", "xresize.py"])

            elif all(k in self.pressed for k in self.execute):
                try:
                    w,h = self.get_text()
                    if w and h:
                        params = f"0,0,0,{w},{h}"
                        subprocess.run(["wmctrl", "-i", "-r", self.window, "-e", params])
                except ValueError:
                    self.setText("Invalid")

    def on_release(self,key):

        self.pressed.discard(key)
        if key == keyboard.Key.esc:
            self.hide()


def get_active_window():
    result = subprocess.run(["xdotool", "getactivewindow"], capture_output=True, text=True)
    if result:
        return result.stdout.strip()
    else:
        raise ModuleNotFoundError


if __name__ == "__main__":
    xApp = QtWidgets.QApplication(sys.argv)
    xApp.setStyleSheet("""
    QLineEdit {
        background-color: rgba(20, 30, 50, 180);
        border: 2px solid rgba(0, 200, 255, 180);
        border-radius: 20px;
        padding: 14px 22px;
        font-size: 18pt;
        color: #b3ffff;
        selection-background-color: rgba(0, 150, 255, 120);
        selection-color: #ffffff;
    }

    QLineEdit:hover {
        border: 2px solid rgba(0, 255, 220, 200);
        background-color: rgba(25, 35, 60, 200);
    }

    QLineEdit:focus {
        border: 2px solid rgba(0, 255, 180, 220);
        background-color: rgba(30, 40, 70, 220);
        color: #a0ffff;
    }
""")

    x = xWindow()
    x.window = get_active_window()
    x.resize(185,50)
    x.show()
    sys.exit(xApp.exec())
