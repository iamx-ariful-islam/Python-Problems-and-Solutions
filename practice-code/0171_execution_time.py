import time


start_time = time.time()
sum_result = sum(range(1, 1000001))
end_time   = time.time()

execution_time = end_time - start_time
print(f'Execution time: {execution_time:.5f} seconds')


'''output:

Execution time: 0.01659 seconds
'''