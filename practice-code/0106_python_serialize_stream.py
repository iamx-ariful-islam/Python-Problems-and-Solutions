import pickle


data = {'country':'Bangladesh', 'Capital':'Dhaka'}

# write data in text file
with open('serialize_data_stream.txt', 'wb') as f:
    pickle.dump(data, f)


# read data from text file
with open('serialize_data_stream.txt', 'rb') as f:
    read_data = pickle.load(f)
    print(read_data)
    
    
'''output:

{'country': 'Bangladesh', 'Capital': 'Dhaka'}
'''