import re

def is_valid_ip(value):
    ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return bool(re.match(ip_pattern, value))


print(is_valid_ip('127.a.1'))
print(is_valid_ip('127.0.0.1'))


'''output:

False
True
'''