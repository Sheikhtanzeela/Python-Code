

try:

	f = open('test.txt')

	#var = bad_var raises exception


	#or we can manually raise exception

	if f.name == 'c.txt':
		raise Exception

except Exception:

	print('Error .!')

except  FileNotFoundError as e:
	print(e)

else:
	print(f.read())
	f.close()

finally:
	print('Executing finally...')