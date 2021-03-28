nums = [1,2,3,4]

for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

for num in nums:
    if num == 3:
        print('Found 3')
        continue
    print(num)


for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range(5):
    print(i)

for i in range(1,11):
    print(i)


# WHILE LOOPS

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1























    
