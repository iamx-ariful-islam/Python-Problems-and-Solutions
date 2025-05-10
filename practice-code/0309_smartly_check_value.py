def return_result(result=True):
    return result


if (result := return_result(False) or '0'):
    print(result)

if (result := return_result() or '0'):
    print(result)
    
    
'''output:

0
True
'''