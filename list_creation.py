nums = [1,2,3,5,6,7,8,9,10]

# list comprehension
my_list = []
for  n in nums:
    my_list.append(n)
    my_list.append(n*n)
print(my_list)

my_list = [n for n in nums]
my_list = [n*n for n in nums]

# using map and lambdas
my_list = map(lambda n : n*n, nums)

# copy even nums
my_list = []
for  n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

my_list = [n for n in nums if n%2 == 0]

my_list = filter(lambda n:n%2 == 0, nums)

# print pairs
my_list = []
for  letter in 'abcd':
    for num in range(4):
        my_list.append((letter, nun))
print(my_list)

my_list = [(letter,num) for letter in 'abcd' for num in range(4)]


# DICTIONARY COMPREHENSION

names = ['tabu', 'sani', 'sonu', 'didi']
heros = ['pilot', 'eng', 'doc', 'teacher']

print zip(names, heros)

my_dcit = []
for  name, hero in zip(names, heros):
    my-dict[name] = hero
print(my_list)

my_dict = {name: hero for name,hero in zip(names,heros)}

# SET COMPREHENSION

# set is like list which has unique values
nums = [1,2,3,5,6,3,2,1,4,4,6,7,3,2,8,4,5,5]

my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set = {n for n in nums}



# GENERATOE EXPRESSIONS

nums = [1,2,3,5,6,7,8,9,4]

def gen_fun(nums):
    for n in nums:
        yield n*n

my_gen = gen_fun(nums)

my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)












































