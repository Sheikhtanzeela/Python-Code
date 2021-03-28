language = 'Java'
if language == 'python':
    print("true")
elif language == 'Java':
    print('I am java')
else:
    print('No match')
if True:
    print("I am True")
if False:
    print("I am false")


# BOOLEAN

user = 'Admin'
logged_in = True


# AND OR NOT  we can use these boolean values
if user == 'Admin' and logged_in:
    print('Admin')
else:
    print('Bad Creds')
if not logged_in:
    print('Please login first')
else:
    print('Welcome!')


#OBJECT IDENTITY : is
a = [1,2,4]
b = [1,2,4]
print(a == b)
print(a is b)  #FALSE because they are different objects in memory
print(id(a))
b = a
print(a is b ) # TRUE now they are same objects in memory


#FALSE VALUES
condition = False                # evluates to false
condition = None                 # evaluates to false
condition =  0                   # evaluates to false
condition = '' or () or []       # evaluates to false
conditon = {}                    # evaluates to false
