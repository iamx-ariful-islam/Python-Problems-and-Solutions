file  = open("file_name.txt", "r")
lines = file.readlines()

for line in lines:
    print(''.join(x[0] for x in line.split()))

file.close()