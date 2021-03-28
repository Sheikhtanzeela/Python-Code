def decorator_fun(origional_fun):
    def wrapper_fun():
        print('Wrapper function ran before '.format(origional_fun.__name__))
        return origional_fun()
    return wrapper_fun

@decorator_fun
def display():
    print('Decorator function ran')

# decorator_display = decorator_fun(display)
# above line means same as @decorator_fun
# decorator_display()
# These 2 lines is replaced by following line after adding @decorator_fun

display()


