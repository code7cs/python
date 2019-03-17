from sys import exit
from random import randint

def death():
	quips = ["You died. You kinda suck at this.",
	"Nice job, you died ...jackass.",
	"Such a luser.",
	"I have a small puppy that's better at this."]

	print quips[randint(0, len(quips)-1)]
	exit(1)

def central_corridor ():

	print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
	print "your entire crew. You are the last surviving member and your last"
	print "mission is to get the neutron destruct bomb from the Weapons Armory,"
	print "put it in the bridge, and blow the ship up after getting into an "
	print "escape pod."
	print "\n"
	print "You're running down the central corridor to the Weapons Armory when"
	print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
	print "flowing around his hate filled body. He's blocking the door to the"
	print "Armory and about to pull a weapon to blast you."

	action = raw_input("> ")

	if action == "shoot!":
		print "Quick on the draw you yank out your blaster and fire it at the Gothon."
		print "His clown costume is flowing and moving around his body, which throws"
		print "off your aim. Your laser hits his costume but misses him entirely. This"
		print "completely ruins his brand new costume his mother bought him, which"
		print "makes him fly into an insane rage and blast you repeatedly in the face until"
		print "you are dead. Then he eats you."

		return 'death'

	elif action == "dodge!":
		print "Like a world class boxer you dodge, weave, slip..."

		return 'death'

	elif action == "tell a joke":
		print "Lucky for you..."

		return 'laser_weapon_armory'

	else:
		print "DOES NOT COMPUTE!"
		return 'central_corridor'

def laser_weapon_armory():
	print "You do a dive roll into the Weapon Armory, crouch and scan the room"
	code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
	guess = raw_input("[keypad]> ")
	guesses = 0

	while guess != code and guesses < 10:
		print "BZZZZEDDD!"
		guesses += 1
		guess = raw_input("[keypad]> ")



































