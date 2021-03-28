li = [9,5,2,4,7,6,8,1,3]


# Sorted function , returns a new list
# gives us flexiblity to pass any args

s_li = sorted(li)         # Ascending order

s_li = sorted(li, reverse=True)     # sorts in reverse order
#print('Sorted list ',s_li) 

# Sorted method , Sorts in place and returns none
# sort method works specifically on list
#li.sort()

li.sort(reverse=True)
#print('Original list',li)



# Sorted functions can be used to any other DS also
# TUPLE
tup = (9,4,2,3,5,7,8,1,6)
s_tup = sorted(tup)
#print('Tuple\t',s_tup)



# DICTIONARY  : sorts only keys
dic = {'name':'corey','job':'progming','age':'20','os':'mac'}
s_dic = sorted(dic)
#print('Tuple\t',s_dic)


# Sort Negative values
li =[-6,-3,5,2,4,-1]
s_li = sorted(li, key=abs)
print(s_li)

# sort objects  : write custom function and define a key

def e_sort(emp):
    return emp.salary
# use key = e_sort

# or use key = lambda e : e.name without e_sort function

# or key =attrpgetter('age')
































