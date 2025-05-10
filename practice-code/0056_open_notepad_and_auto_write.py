# pip install pywinauto

import time
from pywinauto import application


app = application.Application()
app.start('Notepad.exe')
time.sleep(2)
app.Notepad.edit.type_keys(['Hello', 'World'])
time.sleep(2)
app.Notepad.menu_select('File -> SaveAs')
app.SaveAs.edit.set_text('testDemo.txt')
app.SaveAs.Save.click()
time.sleep(2)
app.ConfirmSaveAS.No.click()
app.SaveAs.Cancel.click()
time.sleep(2)
app.Notepad.menu_select('File -> Exit')
time.sleep(2)
app.Notepad.Cancel.click()
time.sleep(2)
app.Notepad.menu_select('File -> Exit')
app.Notepad.DontSave.click()