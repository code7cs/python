# from sys import argv
# from os.path import exists

# script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file , to_file )

# # we could do these two on one line too, how?
# input = open(from_file)
# indata = input.read()

# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exist? %r" % exists(to_file)

# print "Ready, hit RETURN to continue, CTRL -C to abort."
# raw_input ()

# output = open(to_file, 'w')
# output.write (indata)

# print "Alright, all done."

# output.close ()
# input.close()


# ex18.py

# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again (arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two ("Zed","Shaw")
print_two_again ("Zed","Shaw")
print_one ("First!")
print_none()


#ex19.py
def cheese_and_crackers (cheese_count, boxes_of_crackers ):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
	print "We can just give the function numbers directly:"

cheese_and_crackers (20, 30)


print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers (amount_of_cheese , amount_of_crackers )


print "We can even do math inside too:"
cheese_and_crackers (10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers (amount_of_cheese + 100, amount_of_crackers + 1000)










