import pickle


list_data   = [1, 2, 3]
dict_data   = {'a': 1, 'b': 2}
string_data = 'Hello, world'


# saving multiple objects
with open('multiple.pkl', 'wb') as fl:
    pickle.dump(list_data, fl)
    pickle.dump(dict_data, fl)
    pickle.dump(string_data, fl)
    

# loading multiple objects
with open('multiple.pkl', 'rb') as fl:
    loaded_list   = pickle.load(fl)
    loaded_dict   = pickle.load(fl)
    loaded_string = pickle.load(fl)
    
    
print('Loaded List:', loaded_list)
print('Loaded Dictionary:', loaded_dict)
print('Loaded String:', loaded_string)


'''output:

Loaded List: [1, 2, 3]
Loaded Dictionary: {'a': 1, 'b': 2}
Loaded String: Hello, world
'''