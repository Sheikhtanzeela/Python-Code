# GETTER SETTER

first = 'shk'
last = 'tani'
@property
def email():
    return '{}.{}@email.com'.format(first, last)


@fullname.setter
def fullname(self,name):
    first,last = name.split('')
    self.first = fisrt
    self.last = last
fullname = 'Hi Tani'


@fullname.deleter
def fullname(self):
    print('Delete Name!')

print(email())
print(fullname())


del emp_1.fullname
