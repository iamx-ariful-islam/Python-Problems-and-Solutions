def form_integer(number):
    if number < 0:
        print('Please provide a non-negative integer')
        return None
    
    num_str    = str(number)
    num_digit  = len(num_str)
    
    last_digit = int(num_str[-1])
    result     = num_digit * 10 + last_digit
    
    return result

input_number = int(input('Enter a positive integer: '))
new_integer  = form_integer(input_number)
if new_integer is not None:
    print(f'The newly formed integer is: {new_integer}')
    

'''output:

Enter a positive integer: 12
The newly formed integer is: 22
'''