# pip install ipaddress

import ipaddress


def check_private_ip(ip_addr):
    try:
        ip_obj = ipaddress.ip_address(ip_addr)
        return ip_obj.is_private
    except ValueError:
        return False
    

ip_addr = '192.168.0.2'
print(f'Is {ip_addr} private? {check_private_ip(ip_addr)}')



'''output:

Is 192.168.0.2 private? True
'''