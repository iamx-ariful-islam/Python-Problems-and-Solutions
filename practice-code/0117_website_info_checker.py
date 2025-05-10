# pip install request
# pip install python-socket

import json
import socket
import urllib.request


def check_host(info):
    try:
        ipad = socket.gethostbyname(info)
        host = info
    except:
        try:
            ipad = info
            host = socket.gethostbyaddr(info)
        except:
            ipad = info
            host = 'unknown'
    get_info(ipad, host)
    

# get the all information of host address
def get_info(address, host):
    api = "https://freegeoip.app/json/" + address
    try:
        result = urllib.request.urlopen(api).read()
        result = str(result)
        result = result[2:len(result)-3]
        result = json.loads(result)
    except:
        print("Could not find: ", address)
        return None
    
    print("[*] IP Address    : ", result["ip"])
    print("[*] Host Name     : ", host)
    print("[*] Country Name  : ", result["country_name"])
    print("[*] Country Code  : ", result["country_code"])
    print("[*] Region Name   : ", result["region_name"])
    print("[*] Region Code   : ", result["region_code"])
    print("[*] City          : ", result["city"])
    print("[*] Zip Code      : ", result["zip_code"])
    print("[*] Time Zone     : ", result["time_zone"])
    print("[*] Latitude      : ", result["latitude"])
    print("[*] Longitude     : ", result["longitude"])
    print("[*] Metro Code    : ", result["metro_code"])
    print("[*] Location link : ", "https://www.google.com/maps/place/" + str(result["latitude"]) +"," + str(result["longitude"]))


# get ip address info
def ip_address(host):
    print('\n\n[+] Domain Name :', host)
    print('[*] Domain IP   :', socket.gethostbyname(host))
    

# print the help options
def help():
    print('Choose any Option[Search]\n──────────────────────────────────────────')
    print('[1]. IP Address\t[2]. IP Adress Info')
    print('[0]. Exit')
    

# root function
def main():
    help()
    while True:
        num = int(input('\nEnter search option: '))
        if num==1:
            input_site = input('\nEnter any Website|IP Adress: ')
            ip_address(input_site)
        elif num==2:
            input_site = input('\nEnter any Website|IP Adress: ')
            check_host(input_site)
        elif num==0: break
        else: print('Invalid Value')
        
# root
if __name__ == '__main__':
    main()