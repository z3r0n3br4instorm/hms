import os
import sys
print('\33]0;//PROGRAM INSTALL\a', end='')
sys.stdout.flush()
print("//INITIALZING PACKAGE INSTALLER...")
os.system("sudo apt install python-is-python3 && sudo apt install pip3")
print("Internet connection is required")
os.system("pip install PyQt5 && pip install psutil && pip install GPUtil && pip install pyuic5")
