data = r"""
Bytes data format
**********************************************
LF  = Line Feed           = b'\x0A' | b'\n'
CR  = Carriage Return     = b'\x0D' | b'\r'
STX = Start of Text       = b'\x02'
ETX = End of Text         = b'\x03'
EOT = End of Transmission = b'\x04'
ENQ = Enquiry             = b'\x05'
ACK = Acknowledge         = b'\x06'
NAK = Not Acknowledged    = b'\x15'
"""

print(data)


'''output:

Bytes data format
**********************************************
LF  = Line Feed           = b'\x0A' | b'\n'
CR  = Carriage Return     = b'\x0D' | b'\r'
STX = Start of Text       = b'\x02'
ETX = End of Text         = b'\x03'
EOT = End of Transmission = b'\x04'
ENQ = Enquiry             = b'\x05'
ACK = Acknowledge         = b'\x06'
NAK = Not Acknowledged    = b'\x15'
'''