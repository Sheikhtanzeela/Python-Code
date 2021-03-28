def hello_fun():
    print('hello function.')
    
hello_fun()

# function help us reuse code
# DRY don'trepeatyourself

def hello_fun():
    return 'hello function.'
    
print(hello_fun())

# special functions
print(len('Test'))
print(hello_fun().upper())

# pass Arguments
def hello_fun(greeting,name = 'You'):
    return'{}, {}'.format(greeting, name)    
print(hello_fun('Hi', name ='corey')) # Required positional arguments have to come before keyword arguments

# many argumsnts in one variable
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='john', age=20)


def student_info(*args, **kwargs): # passing arbitarilymany number of values
    print(args)
    print(kwargs)
courses = ['Math','Art']
info = {'name' :'john', 'age' : 20}

student_info(*courses,**info) #** used to unpack the values





















