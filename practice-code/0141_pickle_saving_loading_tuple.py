import pickle


my_tuple = (10, 20, 30, 'Bangladesh')

# saving tuple
with open('tuple.pkl', 'wb') as fl:
    pickle.dump(my_tuple, fl)
    

# loading tuple
with open('tuple.pkl', 'rb') as fl:
    loaded_tuple = pickle.load(fl)
    
   
print('Loaded Tuple:', loaded_tuple)


'''output:

Loaded Tuple: (10, 20, 30, 'Bangladesh')
'''