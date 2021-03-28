def prefix_decorator(prefix):
    def decorator_fun(origional_fun):
        def wrapper_fun(*args, **kwargs):
            print(prefix,' Wrapper function ran before '.format(origional_fun.__name__))
            result =  origional_fun(*args,**kwargs)
            print(prefix,' Wrapper function ran After '.format(origional_fun.__name__))
            return result
        return wrapper_fun
    return decorator_fun


#@decorator_fun()
@prefix_decorator('Teting:')
def display_info(name,age):
    print('Decorator function ran')


display_info('john',25)
display_info('Samm',30)
