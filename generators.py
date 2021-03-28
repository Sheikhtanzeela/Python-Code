

def squared_numbers(nums):
	for i in nums:
		yield (i*i)


my_nums = squared_numbers([1,2,3,4,5])


# list comprehension

my_nums = (x*x for x in [1,2,3,4,5])

#print next(my_nums) prints one num at a time 

print list(my_nums)

#for num in my_nums:
#	print(num ,end=' ')