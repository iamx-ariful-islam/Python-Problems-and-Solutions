import os
import winreg as reg 

  
def AddToRegistry():
    file_path   = os.path.dirname(os.path.realpath(__file__))
    script_name = "mYscript.py"     
      
    # joins the file name to end of path address
    address = os.join(file_path, script_name) 
      
    # key we want to change is HKEY_CURRENT_USER 
    # key value is Software\Microsoft\Windows\CurrentVersion\Run
    key = '' # HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
      
    # open the key to make changes to
    open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
      
    # modifiy the opened key
    reg.SetValueEx(open, "any_name", 0, reg.REG_SZ, address)
    reg.CloseKey(open)


# driver code
if __name__=="__main__":
    AddToRegistry()