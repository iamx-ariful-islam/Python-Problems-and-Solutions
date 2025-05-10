import getpass


default_username = 'admin'
default_password = 'admin'

input_username = input('Enter your username: ')
input_password = getpass.getpass('Enter your password: ')

if default_username == input_username and default_password == input_password:
    print('Access Granted. Welcome...!')
else:
    print('Access Denied. Incorrect username or password.')