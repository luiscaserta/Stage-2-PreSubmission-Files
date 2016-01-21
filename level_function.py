level1 = "This is level1!"
level2 = "This is level2!"
level3 = "This is level3!"

def game_level(level):
	input = raw_input("Choose level of game to play (easy, medium, hard): ")
	if input == "easy" or input == "Easy":
		game = level1
		return game
	elif input == "medium" or input == "Medium":
		game = level2
		return game
	elif input == "hard" or input == "Hard":
		game = level3
		return game
	else:
		print "That is not a valid option!!"
		return game_level(level)

print game_level(raw_input)	
