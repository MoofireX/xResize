# 📏 xResize ✨                                                         [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/MoofireX/xResize)

A sleek and simple tool to quickly resize your active window with a keyboard shortcut. Perfect for developers, designers, and anyone who needs to manage window sizes with precision and speed! 🚀

## ⚠️ System Requirements

This tool is designed specifically for **Debian-based Linux distributions** (like Ubuntu, Mint, etc.) using the **X11 display server**. It will not work on Wayland or other operating systems.

## 🛠️ Installation

1.  **Install System Dependencies:**

    This tool relies on `wmctrl` and `xdotool` to manage windows. You can install them using `apt`:

    ```bash
    sudo apt update
    sudo apt install wmctrl xdotool
    ```

2.  **Install Python Libraries:**

    The user interface is built with PySide6 and it uses pynput to listen for keyboard shortcuts. Install them using `pip`:

    ```bash
    pip install PySide6 pynput
    ```

## 🚀 Usage

For `xresize` to work, a listener process must be running in the background to detect the keyboard shortcut.

1.  **Run the listener:**

    To start the listener, run the following command in a terminal:
    ```bash
    python xresize.py
    ```
    This will open a small window. Press the `Esc` key to hide it. The listener will continue to run in the background.

    To keep it running even after you close the terminal, you can use `nohup`:
    ```bash
    nohup python xresize.py &
    ```
    You will still need to press `Esc` on the window that appears.

2.  **Activate the resizer:**

    Once the listener is running, press `Ctrl` + `Alt` + `X` to bring up the resize input field on your active window.

3.  **Enter Dimensions:**

    Type the desired dimensions in `WIDTHxHEIGHT` format (e.g., `1920x1080` or `800x600`).

4.  **Apply:**

    Press `Enter` to resize the window.

5.  **Cancel:**

    Press `Esc` to close the input field without making changes.


## 📜 License

This project is licensed under the GPLv3 License. See the [LICENSE](LICENSE) file for details.
