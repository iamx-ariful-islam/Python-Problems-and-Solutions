import ctypes


FILE_ATTRIBUTE_HIDDEN = 0x02
ctypes.windll.kernel32.SetFileAttributesW('file_name', FILE_ATTRIBUTE_HIDDEN)