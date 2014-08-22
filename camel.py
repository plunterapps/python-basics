import random
#Camel BASIC Game in python from 'Program Arcade Games with Python' Chapter 4: Lab exercise!
#Written by Iago Augusto - plunter.com

print """
Welcome to camel!
You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and out run the natives."""

#VARIABLES
miles_traveled = 0
thirst = 0
camel_tied = 0
natives_travel = -20
canteen = 5
natives_up = random.randrange(0, 10)
full_speed = random.randrange(10, 20)
moderate_speed = random.randrange(5, 12)
#####

done = False
while not done:
	print """
	A. Drink from your canteen.
	B. Ahead moderate speed.
	C. Ahead full speed.
	D. Stop for the night.
	E. Status check.
	Q. Quit.\n"""
	choice = raw_input("What do you want to do? ")
	if choice.upper() == "Q":
		done = True
	
	#STATUS CHECK
	elif choice.upper() == "E":
		print "\nMiles traveled: %s\nDrinks in canteen: %s\nThe natives are %s behind you." % (miles_traveled, canteen, natives_travel)

	#STOP FOR THE NIGHT	
	elif choice.upper() == "D":
		camel_tied = 0
		print "The camel is happy! The natives are %s miles" % natives_up
	
	#AHEAD FULL SPEED
	elif choice.upper() == "C":
		print "You walked %s miles" % full_speed
		miles_traveled = miles_traveled + full_speed
		natives_travel = natives_travel + natives_up
		thirst = thirst + 1
		camel_tied = camel_tied + random.randrange(1,3)

	#AHEAD MODERATE SPEED
	elif choice.upper() == "B":
		print "You walked %s miles" % moderate_speed
		miles_traveled += full_speed
		natives_travel += natives_up
		thirst += 1
		camel_tied = camel_tied + random.randrange(1,3)

	#DRINK FROM YOUR CANTEEN
	elif choice.upper() == "A":
		print "You drink from your canteen."
		canteen = canteen - 1	
		thirst = 0
	
	#PRINT THIRSTY IF THIRST >= 4
	if thirst >= 4:
		print "You are thirsty."

	#DYING OF THIRSTY
	if thirst >= 6:
		print "You died of thirsty."
		done = True

	#PRINT IF CAMEL IS GETTING TIRED
	if camel_tied >= 5:
		print "Your camel is getting tired."
	
	#CAMEL IS DEAD
	if camel_tied >= 8:
		print "Your camel is dead."
		done = True

	#IF NATIVES CAUGHT
	if natives_travel >= 0:
		print "The natives caught you."
		done = True

	#NATIVES WALKING
	elif:
		natives_travel >= -10
		print "Natives are getting close."
		
	if miles_traveled == 200:
		print "You won, you got the camel and across the Mobi Desert."
		done = True
		
	else:
		print "Something is wrong!"
