print(1+2)
print('hi, '+'tanu')


# __this is called dunder

#how our objects are printed and displayed

def __str__(self):
    return '{} - {}'.format(self.fullname(),self.email)

def __repr__(self):
    return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

print(repr(object)) # prints the object
print(str(object))


# 
