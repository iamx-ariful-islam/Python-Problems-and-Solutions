# write text in .txt file
with open('print.txt', 'w') as f:
    print('Nothing to print', file=f)

# read from text file
try:
    file = open('print.txt', 'r')
except Exception as e:
    print(e)
else:
    data = file.read()
    print(data)
finally:
    file.close()