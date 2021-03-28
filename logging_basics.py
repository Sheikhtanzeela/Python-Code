import logging

def add(a,b):
	return a+b


def sub(a,b):
	return a-b


def mul(a,b):
	return a*b


def div(a,b):
	return a/b


num_1 = 10
num_2 =5

add_result = add(num_1,num_2)
logging.debug('Add : {} + {} = {}'.format(num_1,num_2,add_result))

sub_result = sub(num_1,num_2)
logging.debug('sub : {} - {} = {}'.format(num_1,num_2,sub_result))

mul_result = mul(num_1,num_2)
logging.debug('mul : {} * {} = {}'.format(num_1,num_2,mul_result))

div_result = div(num_1s,num_2)
logging.debug('div : {} / {} = {}'.format(num_1,num_2,div_result))