class test:
    
    @staticmethod
    def get_name():
        __name = 'python3.x'
        return __name


cls_obj = test() # cls_obj = test
print(cls_obj.get_name())


'''output:

python3.x
'''