# 📏 xresize ✨

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

1.  **Run the script:**

    ```bash
    python xresize.py
    ```

2.  **Activate the resizer:**

    Press `Ctrl` + `Space` to bring up the resize input field on your active window.

3.  **Enter Dimensions:**

    Type the desired dimensions in `WIDTHxHEIGHT` format (e.g., `1920x1080` or `800x600`).

4.  **Apply:**

    Press `Enter` to resize the window.

5.  **Cancel:**

    Press `Esc` to close the input field without making changes.

## 📜 License

This project is licensed under the GPLv3 License. See the [LICENSE](LICENSE) file for details.
