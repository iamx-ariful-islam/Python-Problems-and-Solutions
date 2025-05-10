import inspect


def fist_function():
    parent_func_name = inspect.stack()[1].function
    print('Call from:', parent_func_name)
    
    
def second_function():
    # call the test1 function
    fist_function()
    
second_function()

'''output:

Call from: second_function
'''