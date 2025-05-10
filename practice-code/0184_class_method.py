class test:
    __name = 'python3.x'
    
    @classmethod
    def get_name(cls):
        return cls.__name


cls_obj = test # if use @classmethod then use test() or test
print(cls_obj.get_name())

# or

class test:
    __name = 'python3.x'

    def get_name(self):
        return self.__name


cls_obj = test() # if not use @classmethod then use test()
print(cls_obj.get_name())


'''output:

python3.x
python3.x
'''