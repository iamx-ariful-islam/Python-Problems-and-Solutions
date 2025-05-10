import timeit


# set approach
my_set = {1, 2, 3, 4, 5}
def set_lookup():
    return 5 in my_set


# dictionary approach
my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
def dict_lookup():
    return 5 in my_dict


# time measurement
set_time  = timeit.timeit(set_lookup, number=10000000)
dict_time = timeit.timeit(dict_lookup, number=10000000)


print('Set time:', set_time)
print('Dictionary time:', dict_time)



'''output:

Set time: 0.49953120001009665
Dictionary time: 0.5197396999865305
'''