import os
from time import sleep
import wmi
import getpass
from pathlib import Path
import shutil
import sys
import re
import subprocess
import win32file
from ctypes import windll

USER_NAME = getpass.getuser()

def get_device_list():
    out = os.popen('adb devices').read()
    return list(filter(lambda d: d.endswith('device'), out.split('\n')))    

# Due this line we can't assign this script filename (current: main.py) to `python.py` otherwise we won't be able to recognize if it's being ran by Python interpreter or by Windows .exe, see this answer for details: https://stackoverflow.com/questions/50959340/pyinstaller-exes-file-refers-to-a-py-file.
SCRIPT_EXECUTABLE_FILENAME = '.'.join(os.path.basename(__file__).split('.')[0:len(os.path.basename(__file__).split('.')) - 1]) + '.exe'
IS_EXECUTABLE = os.path.basename(sys.executable) == SCRIPT_EXECUTABLE_FILENAME

def on_device_connected(*devices):
    try:
        print(f'New device connected')
        os.system('adb shell svc usb setFunctions rndis')
        print('USB Tethering command was executed...')
    except:
        pass


def get_file_path_of_this_script():
    return os.path.realpath(sys.executable if IS_EXECUTABLE else __file__)

def listen_for_usb_devices():
    print('Listening for devices...')

    last_devices = get_device_list()

    on_device_connected()

    while True:
        devices = get_device_list()

        if len(last_devices) == len(devices): 
            pass # no changes detected
        elif len(last_devices) > len(devices): 
            print('Some device was removed')
        elif len(last_devices) < len(devices):
            on_device_connected(*devices[len(last_devices) - 1:])

        last_devices = [*devices]



def create_copy_of_this_script_on_startup_windows_folder():
    try:
        if IS_EXECUTABLE:
            if sys.executable.startswith(f'C:\\Users\\{USER_NAME}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'):
                return print('This is an automatic execution, skipping this step.')

        script_temp_filepath = get_file_path_of_this_script()

        script_filename = os.path.basename(get_file_path_of_this_script())

        script_folderpath = os.path.dirname(get_file_path_of_this_script())

        permanent_script_filepath = f'C:\\Users\\{USER_NAME}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{script_filename}'

        if Path(permanent_script_filepath).is_file():
            os.unlink(permanent_script_filepath)
            print(f'Deleted old script at {permanent_script_filepath}')

        shutil.copyfile(script_temp_filepath, permanent_script_filepath)

        print(f'Script copied to {permanent_script_filepath}')
    except Exception as e:
        print('Error: %s' % e)

try:
    create_copy_of_this_script_on_startup_windows_folder()
    listen_for_usb_devices()
except Exception as e:
    print(f'Fatal Error: {e}')
finally:
    input('Press enter to exit...')
