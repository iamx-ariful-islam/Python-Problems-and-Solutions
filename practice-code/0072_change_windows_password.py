import sys
import subprocess as sp

# from user passing arguments
user, password = sys.argv[1:]

password = password.encode() + b'\n'

subk = dict(stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE)
pwd_change = sp.Popen(['passwd', user], **subk)

for x in range(2):
    pwd_change.stdin.write(password)