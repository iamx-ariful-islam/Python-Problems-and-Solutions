import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
    
person = Person('John', 15)

# saving person objects
with open('person.pkl', 'wb') as fl:
    pickle.dump(person, fl)
    

# loading person objects
with open('person.pkl', 'rb') as fl:
    loaded_person = pickle.load(fl)
    
   
print('Loaded Person:', loaded_person)


'''output:

Loaded Person: Person(name=John, age=15)
'''