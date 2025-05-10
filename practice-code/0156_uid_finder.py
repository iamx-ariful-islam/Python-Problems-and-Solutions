# pip install b64uuid

import os
import uuid
from b64uuid import B64UUID


UUID = uuid.uuid1()

print("UUID is ", UUID)
print("UUID Type is ",type(UUID))
print('UUID.bytes   :', UUID.bytes)
print('UUID.bytes_le :', UUID.bytes_le)
print('UUID.hex     :', UUID.hex)
print('UUID.int     :', UUID.int)
print('UUID.urn     :', UUID.urn)
print('UUID.variant :', UUID.variant)
print('UUID.version :', UUID.version)
print('UUID.fields  :', UUID.fields)
print("Prining each field seperately")
print('UUID.time_low            : ', UUID.time_low)
print('UUID.time_mid            : ', UUID.time_mid)
print('UUID.time_hi_version     : ', UUID.time_hi_version)
print('UUID.clock_seq_hi_variant: ', UUID.clock_seq_hi_variant)
print('UUID.clock_seq_low       : ', UUID.clock_seq_low)
print('UUID.node                : ', UUID.node)
print('UUID.time                : ', UUID.time)
print('UUID.clock_seq           : ', UUID.clock_seq)
print('UUID.SafeUUID           : ', UUID.is_safe)

print(uuid.getnode())


msg = """hello [%s],
all your personal files, photos, videos 'n other important documents have been encrypted.
your private decryption key has ben created 'n stored on a secure anonymouse server,
if you don't pay, the files will be lost.
""" % os.getlogin()
print(msg)

choice = input('Enter [Y/n] to Binary: ').lower()

if choice == 'y' or choice == 'yes' or choice == '1':
    bmsg = ' '.join(format(ord(x), 'b') for x in msg)
    print(bmsg)

uid = uuid.uuid1()
bid = B64UUID(uid)
print(bid)
print(uid)