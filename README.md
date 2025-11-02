# 📏 xResize ✨

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

    Press `Ctrl` + `Alt` + `X` to bring up the resize input field on your active window.

3.  **Enter Dimensions:**

    Type the desired dimensions in `WIDTHxHEIGHT` format (e.g., `1920x1080` or `800x600`).

4.  **Apply:**

    Press `Enter` to resize the window.

5.  **Cancel:**

    Press `Esc` to close the input field without making changes.

## 📦 Installing as a Desktop Application

To have `xresize` available as a system-wide command and automatically start when you log in, you can install it as a desktop application using the provided `.deb` package.

### 1. Install the Package

The `.deb` package is located in the `dist` directory. You can install it using `dpkg`:

```bash
sudo dpkg -i dist/xresize.deb
```

If you encounter any dependency issues, run the following command to fix them:

```bash
sudo apt-get install -f
```

This will install `xresize` as a system application, making the `xresize` command available globally.

### 2. Run on Startup

To have `xresize` launch automatically at login, you need to create a `.desktop` file in your `~/.config/autostart/` directory.

Create the file `~/.config/autostart/xresize.desktop` and add the following content:

```ini
[Desktop Entry]
Name=xResize
Comment=A tool to quickly resize your active window with a keyboard shortcut.
Exec=xresize
Type=Application
Terminal=false
```

You can create this file using your favorite text editor, or by running the following command:

```bash
mkdir -p ~/.config/autostart && printf '[Desktop Entry]\nName=xResize\nComment=A tool to quickly resize your active window with a keyboard shortcut.\nExec=xresize\nType=Application\nTerminal=false\n' > ~/.config/autostart/xresize.desktop
```

After creating the file, `xresize` will start automatically the next time you log in.

## 📜 License

This project is licensed under the GPLv3 License. See the [LICENSE](LICENSE) file for details.
