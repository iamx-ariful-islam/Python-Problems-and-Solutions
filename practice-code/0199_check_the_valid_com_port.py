def is_valid_com(value):
    return value.startswith('COM') and value[3:].isdigit()


print(is_valid_com('COM'))
print(is_valid_com('COM2'))
print(is_valid_com('ABC'))


'''output:

False
True
False
'''