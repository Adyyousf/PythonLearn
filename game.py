from sys import exit

def start():
	"""Start the game and ask for the doors to be opened""" 

	print "\n\tWELCOME TO THE GAME OF LIFE\n"
	start_message =  """
	You're given three doors.
	
	1 > The door of life 
	2 > The door of death
	3 > The door of idk
	
	"""
	print(start_message)
	option = int(raw_input("Choose one > "))
	
	if option == 1 :
		door_1()
	elif option == 2 :
		door_2()
	elif option == 3 :
		door_3()
	else :
		print "\nERROR! Not within range.\n"
		confirm = raw_input("Try again? (Y/N) > ")
		
		if confirm == 'y' and 'Y':
			start()
		else : 
			exit(0)
			
def door_1(): 
	""" Door 1 the door of life """
	print "\n\tWelcome to the door of Life."
	print "\tIn Life Your choice of people matters the most\n"
	print "\tI give you a choice to choose. Choose wisely. \t\n1> Friend? \n2> GF/BF? "
	choice = int(raw_input("What do you choose? 1 or 2? > "))
	if choice == 1 :
		friend()
	elif choice == 2 :
		gf()
	else :
		print "Wrong option!!"
		exit(0)
		
def friend():
	"""Type of friend"""
	print "\tYou choose friend. Good choice. But That's not it. The character matters."
	print "\tYou've two options for the type of friend. choose one.\n\t1> Fun loving\n\t2> Focused"
	choice = int(raw_input("What's your choice. 1 or 2? > "))
	if choice == 1 :
		print "So you want to Enjoy Life"
		print "Could've been a good choice but you're going broke eventually\n\tOr maybe you already are!!!"
	elif choice == 2 :
		focused()
	else :
		"Wrong option!!"
		exit(0)

start()