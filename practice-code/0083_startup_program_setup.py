import os
import winreg


# root class
class AddToRegistry:
    def __init__(self):
        self.AutoRun()
        

    def AutoRun(self):
        fPath = os.path.dirname(os.path.realpath(__file__))
        fName = 'mni.exe'

        fFile = os.path.join(fPath, fName)
        key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
          
        open = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_value, 0, winreg.KEY_ALL_ACCESS)
          
        winreg.SetValueEx(open, "OpenMNI", 0, winreg.REG_SZ, fFile)
        winreg.CloseKey(open)
        

# root
if __name__ == "__main__":
    AddToRegistry()