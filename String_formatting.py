person  = {'name':'john','age':23}

# 1
sentence = 'My name is ' + person['name']+ ' and I am '+str(person['age'])+' years old

# 2
sentence = 'My name is {} and I am {} years old'.format(person['name'],person['age'])

# Or we can write place holders  in the brace.0,1,2,3...

tag = 'h1'
text = 'this is a headline'

# 3
sentence = '<{0}> {1}</{0}>'.format(tag,text)

# 4
sentence = 'My name is {0[name]} and I am {1[age]}years old'.format(person,person)

# 5
{0.name}{0.age}....


# usualyused for dictionaries

{name}{age}.format(name='', age='')

# {name}{age}.format(**person)

# FORMAT NUMBERS

fori i in range(1,11):
    sen = 'The vale is {0:2}'.format(i)
    print(sen)

# decimal pi = 3.12233
sen = 'pi is {:.3f}'.format(pi)

# seperated by a character
sen = '{:,}'.format(100**2)




















