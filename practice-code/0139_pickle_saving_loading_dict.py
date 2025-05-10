import pickle


my_dict = {'name': 'John', 'age': 15, 'city': 'Bangladesh'}

# saving dictionary
with open('dict.pkl', 'wb') as fl:
    pickle.dump(my_dict, fl)
    

# loading dictionary
with open('dict.pkl', 'rb') as fl:
    loaded_dict = pickle.load(fl)
    
   
print('Loaded Dictionary:', loaded_dict)


'''output:

Loaded Dictionary: {'name': 'John', 'age': 15, 'city': 'Bangladesh'}
'''