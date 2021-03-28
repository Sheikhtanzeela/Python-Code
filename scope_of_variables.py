'''
LEGB
Local , Enclosing, Global , Built-in
'''

# LOCAL : variables defined within a function

# ENCLOSING :  local scope of enclosing function

# GLOBAL : Variables decleared global or defined at top level of module

# BUILT-IN : pre-assigned in python

 # global and local scope
 
#x = 'global x'

#def test():
    #global x       not used mostly
 #   x = 'local x'
  #  print(x)
   # print(y)
   
#test()
#print(x)



def test(z):
    x = 'local x'
    print(z)
    
#test('local z')
#print(z)


# Built-in scope

import builtins

#print(dir(builtins))

#m = min([5,1,4,2,3])
#print(m)


# Enclosing scope , occurs where we have function in function .

def outer():
    x = 'outer x'

    def inner():
        nonlocal x     # affects the enclosing scope,, often used
                        #than global scope
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()




































