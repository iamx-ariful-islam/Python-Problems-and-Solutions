# don't use loops at all

for i in range(1, 6):
    print('Python' * i)


nums = [10, 15, 20, 25, 30, 35, 40, 45, 50]

result = 0
for x in nums:
    result += x
print(result)


# use sum
result = sum(nums)
print(result)


#-------------------------------------------


for idx in range(len(nums)):
    print(idx, nums[idx])

    
# use enumerate
for idx, val in enumerate(nums, start=1): # default index start to 0, you want to change that using start=1
    print(idx, val)


#-------------------------------------------


a = [1, 2, 3]
b = ['a', 'b', 'c']

for idx in range(len(a)): # work good, if elements are equal else error (Exp. a=[1, 2, 3, 4], b=['a', 'b', 'c'])
    print(a[idx], b[idx])


# use zip
for v1, v2 in zip(a, b): # there is no error, but use strict=True(Py v10.x) for error
    print(v1, v2)


#-------------------------------------------


events = [('Learn', 5), ('Learn', 15), ('Relaxed', 20)]
mints_studied = 0
for event in events:
    if event[0] == 'Learn':
        mints_studied += event[1]
print(mints_studied)


# use generator
study_times = (event[1] for event in events if event[0]=='Learn')
print(study_times)
print(type(study_times))
mints_studied = sum(study_times)
print(mints_studied) # if you want to print again study_times then generator empty


#-------------------------------------------


lines = ['line1', 'line2', 'line3', 'line4', 'line5', 'line6', 'line7', 'line8']
for i, line in enumerate(lines):
    if i>= 5: break
    print(line)
print()


# use itertools
from itertools import islice

first_five_lines = islice(lines, 5) # you can use range type islice(lines, 1(start), 5(end), 2(iterval))
for line in first_five_lines:
    print(line)
# if you want to print again first_five_lines then itertools empty


#-------------------------------------------


data =  'ABCDEF'
for i in range(len(data)-1):
    print(data[i], data[i+1])
print()


# use itertools
from itertools import pairwise
for pair in pairwise(data):
    print(pair[0], pair[1])


#-------------------------------------------


data = [1, 3, 5, -1, 2, 4]
for item in data:
    if item >= 0:
        print(item)
    else: break
print()

# use itertools
from itertools import takewhile
items = takewhile(lambda x: x >= 0, data)
for item in items:
    print(item)


#-------------------------------------------


vec_a = [1, 3, 5]
vec_b = [2, 4, 6]

result = 0
for v1, v2 in zip(vec_a, vec_b):
    result += v1*v2
print(result)

# use numpy
import numpy as np
result = np.dot(vec_a, vec_b)
print(result)

N = 10_0_0_0
print(N, type(N))

def sum_python():
    return sum(range(N))

def sum_numpy():
    return np.sum(np.arange(N))

print(sum_python())
print(sum_numpy())

import timeit # for calculate time
print('Sum Python:', timeit.timeit(sum_python, number=1))
print('Sum Numpy:', timeit.timeit(sum_numpy, number=1))