## What's it?

This Python script enables USB Tethering when a USB device is connected on Windows, the script runs automatically on startup being required to run manually only once.

The scenario:

1. I connect my android device through USB.
2. Enable USB tethering.
3. Disconnected device from USB.
4. Reconnect the android device also through USB.
5. USB tethering is disabled.

The expected behavior was to keep the USB thetering through the sessions.

So this script will manually enable USB tethering when connecting to my PC.

```shell
# .exe running from startup, so skip the step of copying itself to the startup folder
This is an automatic execution, skipping this step.

# Start pooling for devices through adb
Listening for devices...

# First pooling call adb devices which starts the daemon server
* daemon not running; starting now at tcp:5037
* daemon started successfully

# Trigger the callback
New device connected

# Then enable USB tethering through adb
USB Tethering command was executed...

# Removed device callback (does nothing but notificate)
Some device was removed

# So on...
New device connected
USB Tethering command was executed...
Some device was removed
New device connected
USB Tethering command was executed...
Some device was removed
New device connected
USB Tethering command was executed...
```

## Source

Project based on:

- [Activate USB tethering from the command line](https://android.stackexchange.com/questions/29954/activate-usb-tethering-from-the-command-line).

- [How to start a python file while Windows starts?](https://stackoverflow.com/questions/4438020/how-to-start-a-python-file-while-windows-starts)

- [How do I get the path of the Python script I am running in?](https://stackoverflow.com/questions/595305/how-do-i-get-the-path-of-the-python-script-i-am-running-in)

- [How can I make a Python script standalone executable to run without ANY dependency?](https://stackoverflow.com/questions/5458048/how-can-i-make-a-python-script-standalone-executable-to-run-without-any-dependen)

## Build/Run the script locally

> **Warning** do not forget to create the virtual environment and activate it.

- Clone repository `git clone <this-repo-url> && cd <this-repo-name>`.

Install following packages:

- Install pywin32: `pip install pywin32`.
- Install the current/last version (1.5) of the WMI module from https://github.com/tjguk/wmi `pip install -e git+https://github.com/tjguk/wmi.git#egg=wmi`.

To generate the Windows executable `.exe` (you can skip this section if you plan to run the script using the Python interpreter):

- Install `PyInstaller` by running `pip install pyinstaller`.
- Generate the executable by running: `pyinstaller -F main.py`.
- Execute the `.exe` version of this script located in `dist/main.exe` with administrative powers (required since it will create a file within `...\Windows\Start Menu\Programs\Startup`).

## Environment

Sometimes the environment info is useful to track version conflicts:

```
Python 3.10.5
Windows 10 Pro
```
