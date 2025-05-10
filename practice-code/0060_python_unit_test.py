import unittest


def sum_num(x, y):
    return x+y

def sub_num(x, y):
    return x-y


class MathTestCase(unittest.TestCase):
    def test_sum_num(self): # test word add before function name is mandatory
        result = sum_num(7, 5)
        self.assertEqual(result, 12)

    def test_sub(self):
        result = sub_num(7, 5)
        self.assertTrue(result == 2)
        

class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def full_name(self):
        return self.fname + self.lname


class StrintTestCase(unittest.TestCase):
    def setUp(self): # set anythings
        self.obj = Name('Bangla', 'desh')

    def test_fullname(self):
        name = self.obj.full_name()
        self.assertEqual(name, 'Bangladesh')

    def test_fullname_len(self):
        length = len(self.obj.full_name())
        self.assertTrue(length == 10)

    def tearDown(self): # finally need anythings
        pass


# root
if __name__=='__main__':
    unittest.main()
    

'''output:

....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
'''