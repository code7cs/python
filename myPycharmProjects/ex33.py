def add_number(count, plus_num):
	"""use while loop"""
	i = 0
	numbers = []
	while i < count:
		print "At the top i is %d" % i
		numbers.append(i)
		i = i + plus_num
		print "Numbers now: ", numbers
		print "At the bottom i is %d \n" % i 

	print "The numbers:"
	for num in numbers:
		print num

def add_number_2(count, plus_num):
	"""use for loop"""
	i = 0
	numbers = []
	for i in range(0, count, plus_num):
		print "At the top i is %d" % i
		numbers.append(i)
		print "Numbers now: ", numbers
		print "At the bottom i is %d \n" % i 
	
	print "The numbers:"
	for num in numbers:
		print num

add_number(15, 3)
print "---------------------------"
add_number_2(15, 3)