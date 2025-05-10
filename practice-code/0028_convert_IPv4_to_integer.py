# convert IPv4 to integer number
def Convert(s):
    digits = [int(x) for x in s.split('.')]
    shift = [24, 16, 8, 0]
    for i in range(4):
        digits[i] <<= shift[i]
        print(digits)
    return sum(digits)


# enter IPv4 IP
ipaddr = input('Enter your ip: ')
result = Convert(ipaddr)
print(result)


'''output:

Enter your ip: 127.0.0.1
[2130706432, 0, 0, 1]
[2130706432, 0, 0, 1]
[2130706432, 0, 0, 1]
[2130706432, 0, 0, 1]
2130706433
'''