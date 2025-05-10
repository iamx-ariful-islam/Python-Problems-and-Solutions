# used to pass a non-keyworded, variable-length argument list

def ArgsFunc(*args):
    for v in args:
        print(v)

ArgsFunc('Data', 'Science', 'School')
ArgsFunc('1', 2, 3.3)

# used to pass a keyworded, variable-length argument list

def KWFunc(**kwargs):
    for k, v in kwargs.items():
        print('%s \t= %s'%(k, v))

KWFunc(First='Data', mid='Science', last='School')

# used to pass a non-keyworded and a keyworded variable-length argument list

def KWArgs(*args, **kwargs):
    for v in args:
        print(v)
    for k, v in kwargs.items():
        print(k, '\t=', v)

KWArgs('Data', 'Science', 'School')
KWArgs(First='Data', Mid='Science', Last='School')


'''output:

Data
Science
School

1
2
3.3

First   = Data
mid     = Science
last    = School

Data
Science
School

First   = Data
Mid     = Science
Last    = School
'''