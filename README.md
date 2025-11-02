XResize :: Precision Window Control

<p align="center">
<img alt="License" src="https://www.google.com/search?q=https://img.shields.io/badge/License-GPLv3-blue.svg%3Fstyle%3Dfor-the-badge%26logo%3Dgnu%26logoColor%3Dwhite">
<img alt="Platform" src="https://www.google.com/search?q=https://img.shields.io/badge/Platform-Ubuntu_|_X11-E0540E.svg?style=for-the-badge&logo=ubuntu&logoColor=white">
<img alt="Python" src="https://www.google.com/search?q=https://img.shields.io/badge/Python-3.x-3776AB.svg%3Fstyle%3Dfor-the-badge%26logo%3Dpython%26logoColor%3Dwhite">
<img alt="Framework" src="https://www.google.com/search?q=https://img.shields.io/badge/UI-PySide6-27A9E2.svg%3Fstyle%3Dfor-the-badge%26logo%3Dqt%26logoColor%3Dwhite">
</p>

<p align="center"> <strong>Resize anything. Simple as that.</strong> </p>

<p align="center">
<img src="https://www.google.com/search?q=https://placehold.co/700x120/141E32/00FFFF%3Ftext%3D1920x1080%26font%3Dorbitron" alt="XResize UI Preview">
</p>

:: TRANSMISSION ::

Stop wrestling with window borders. XResize is a lightweight, high-speed utility for the X11 desktop environment, designed to give you surgical control over your workspace. Summon the resize interface with a keypress, input your target dimensions, and execute. Your window obeys.

This tool is built for speed, precision, and minimal distraction, integrating directly with your window manager via wmctrl and xdotool.

:: FEATURES ::

Hotkey Driven: Summon the resize prompt with Left-Ctrl + Space.

Active Window Targeting: Automatically detects and targets the window you're currently using.

Intuitive Input: Accepts dimensions in WIDTHxHEIGHT or WIDTH HEIGHT formats (e.g., 1920x1080 or 1920 1080).

Sleek UI: A minimal, frameless, futuristic-themed prompt (built with PySide6) that appears, does its job, and vanishes.

Instant Execution: Press Enter to resize or Esc to abort.

⛔ :: VITAL SYSTEM REQUIREMENT :: ⛔

This application interfaces directly with the X Window System.

PLATFORM: This tool is designed only for Linux systems running X11.

INCOMPATIBILITY: It will not function on Wayland, Windows, or macOS.

DEPENDENCIES: Requires wmctrl and xdotool to be installed on the host system.

PRIMARY OS: Developed and tested on Ubuntu (X11 Session).

:: INSTALLATION PROTOCOL ::

Execute these commands in your terminal to integrate XResize.

1. System-Level Dependencies (Interface Tools)

These tools are non-negotiable. They provide the low-level interface to the X Window System.

sudo apt update
sudo apt install wmctrl xdotool


2. Python-Level Dependencies (Core & UI)

These Python packages power the hotkeys and the user interface.

pip install PySide6 pynput


3. Acquire the Source Code

Clone this repository to your local machine.

git clone [https://github.com/YOUR_USERNAME/XResize.git](https://github.com/YOUR_USERNAME/XResize.git)
cd XResize


(Don't forget to replace YOUR_USERNAME with your actual GitHub username!)

:: OPERATIONAL GUIDE ::

Launch the Service:
Run the script from your terminal. It's best to run it as a background process.

python xresize.py &


(Tip: Add this command to your startup applications to launch XResize automatically at login.)

Summon Interface:
When focused on any window you wish to resize, press:
Left-Ctrl + Space

Input Target Dimensions:
The XResize prompt will appear. Type your desired resolution.

1920x1080

800 600

3440x1440

Execute Resize:
Press Enter. The active window will instantly snap to the specified dimensions.

Abort Operation:
Press Esc to close the prompt without making any changes.

:: LICENSE ::

This project is licensed under the GNU General Public License v3.0.
See the LICENSE file for full details.

<p align="center">
<a href="https://www.gnu.org/licenses/gpl-3.0.en.html">
<img alt="GPLv3 License" src="https://www.google.com/search?q=https://img.shields.io/badge/License-GPLv3-blue.svg%3Fstyle%3Dfor-the-badge%26logo%3Dgnu%26logoColor%3Dwhite">
</a>
</p>
