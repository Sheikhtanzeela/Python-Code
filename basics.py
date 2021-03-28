#STRING MANIPULATION

#greeting = 'Hello'
#name = 'Tania'
#message = greeting +", "+ name +'Welcome'
#message ='{}, {}. Welcome!'.format(greeting,name)
#message = f'{greeting}, {name.upper()}. Welcome!'
#print(message)
#print(help(str))
#print(help(str.lower))
#print(dir(name))
#print(message.find('hello'))
#print(message.count('l'))
#message = message.replace('' ,''[)
#print(message)

#INTEGERS AND FLOATS


#print(3 / 2)      # 1.5
#print(3 // 2)     # 1 drops the decimal
#print(3 ** 2)     # 3 square

#print(abs(-3))  #removes signs
#print(round(3.78))
#print(round(3.78,1))  # round first digit after decimal

#casting
#m= '100'
#n = '200'

#n = int(n)
#m = int(m) 
#print(n + m)


#LIST

courses = ['Math','Computer','Sciene','Physics','History']
courses_2 = ['Edu','Civic']
#courses.append('art')
#courses.insert(0,courses_2) # inserts list
#courses.extend(courses_2)  # inserts individual item
#courses.insert(0,'Bio')  # inserts at position 0
#print(len(courses))
#print(courses)
#print(courses[3])
#print(courses[-1])    # [-index] gives last item
#print(courses[0:2])
#print(courses[2:])
courses.remove('Math')
courses.pop()  #removes last item from list
print(courses)
courses.reverse()  # reverses list
courses.sort() # sorts alphabetically
courses.sort(reverse=True)
sorted_courses = sorted(courses)   # nicer way to sort
print(sorted_courses)
print(min(nums))
print(max(nums))

print(courses.index('Science'))  #index where course is found
print('Art' in courses)  # boolean value result

for item in courses:     # access values 
    print(item)
    
for index, course in enumerate(courses, start = 1):    #access values and index both
    print(index, course)                               # start value isoptional

course_str = ' , '.join(courses)   # String version of courses
print(course_str)

new_list =course_str.split(' , ')    #turns String back into list


# TUPLES , similar to lists but immutable

tuple_1 = ('Hist','Art','Math','Comsci')

# SET  unordered values

course = {'Math','Hist','CompSci','Art','Polti'}

print('Math' in courses)   # sets use this efficiently

course_2 ={'SE','TOC','Comp','Digital'}

print(course.intersection(course_2))   # common courses

print(course.difference(course_2))     #in courseonly

print(course.union(course_2))

#EMPTY LIST SETS TUPLES

empty_list = []
empty_list = list()

empty_tuple =()
empty_tuple =tuple()

empty_set = set()

#Dictionary

student = {'name':'Tannu', 'age':25, 'courses':['Math','Art']}

print(student['name'])

print(student.get('name'))

print(student.get('phone','Not found'))  # default vlue for keys thatdont exist

student['phone'] = '222 554' # we can do this as below

student.update({'name':'jain','p':34,'age':89})

del student['age']  #delete key
age = student.pop('age')  # return deleted value

print(len(sudent))  #length of dictionary

print(student.keys()) # keys

print(student.items()) # keys + value

for key, value in student.items():
    print(key, value)







