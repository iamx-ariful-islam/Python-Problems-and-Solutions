from queue import Queue

# defined the queue
queue = Queue()

# put the data into queue
queue.put([1, 2, 3, 4, 5])

# get the data from queue
data = queue.get()

print(data)


'''output:

[1, 2, 3, 4, 5]
'''