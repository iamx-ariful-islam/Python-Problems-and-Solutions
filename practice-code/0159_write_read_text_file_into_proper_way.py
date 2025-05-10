# text file automatically close

try:
    with open('close.txt', 'w') as f:
        f.write('Close')
except Exception as e:
    print('File error: ', e)


# text file close manually

# file = type('', (), {})() # declare empty object
# print(file, type(file))

try:
    file = open('close3.txt', 'r') # error
except Exception as e:
    print('File error: ', e)
else:
    txt = file.read()
    print(txt)
finally:
    # if occurs any error
    try: file.close()
    except: pass