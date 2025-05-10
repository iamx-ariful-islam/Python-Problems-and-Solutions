import re

def validate_ip_address(ip_address):
    pattern = r'^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
    return re.match(pattern, ip_address) is not None


print(validate_ip_address('127.a.1'))
print(validate_ip_address('127.0.0.1'))


'''output:

False
True
'''