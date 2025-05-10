import pickle


my_list = ['Hello', 20, 30.50, 'Bangladesh']

# saving list
with open('list.pkl', 'wb') as fl:
    pickle.dump(my_list, fl)
    

# loading list
with open('list.pkl', 'rb') as fl:
    loaded_list = pickle.load(fl)
    
   
print('Loaded List:', loaded_list)


'''output:

Loaded List: ['Hello', 20, 30.5, 'Bangladesh']
'''