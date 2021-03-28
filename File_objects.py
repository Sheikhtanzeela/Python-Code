
# Context Managers
# Automatically closes file
# access files only within this block

#with open('test.txt','r') as f: 

#	f_content = f.read(100)       # 100 = number of characters 
#	print(f_content,end='')

#	for line in f:
#		print(line,end='')

	#f_content = f.readline()
	#print(f_content,end='')

	#size_to_read = 10  

	#f_content = f.read(size_to_read)
	#print(f_content,end='*')

	#f.seek(0)

	#f_content = f.read(size_to_read)
	#print(f_content)

	#print(f.tell())

	#while len(f_content) > 0:
	#	print(f_content, end='*')
	#	f_content = f.read(size_to_read)


#with open('test2.txt','w') as f:
#	f.write('Test')
#	f.seek(0)				# over wites same thing
#	f.write('Test')


with open('test.txt','r') as rf:
	with open('test_copy.txt', 'w') as wf:
		#for line in rf:
		#	wf.write(line)

		#or
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)


