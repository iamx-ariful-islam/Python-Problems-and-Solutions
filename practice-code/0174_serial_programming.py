# pip install pyserial

import serial


serial_connect = serial.Serial('COM1', baudrate=19200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
if serial_connect.is_open:
    print('Port is open')
serial_connect.read(1) # bytes size

serial_connect.close()