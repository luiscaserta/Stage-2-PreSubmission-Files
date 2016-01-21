easy_test = "My name is __1__. I was born in __2__, in __3__. I am presently __4__ years old."
easy_answers = ["Luis", "New Orleans", "1975", "40"]
blanks = ["__1__", "__2__", "__3__", "__4__"]

medium_test = "I have four siblings. Their names are __1__, __2__, __3__, and __4__."
medium_answers = ["Maria", "Paolo", "Anamaria", "Piero"]

hard_test = "I am married.  My wife, Lise is from __1__.  We have two children - __2__ and __3__.  We presently all live in __4__."
hard_answers = ["Quebec, Canada", "Gabrielle", "Emilie", "Montreal"]

def game_level(level):
  input = raw_input("Choose level of game to play (easy, medium, hard): ")
  tries = raw_input("Please enter the number of guesses you would like for each blank: ")
  tries = int(tries)
  if input == "easy" or input == "Easy":
    test = easy_test
    answer = easy_answers
    blank = blanks
    play_game(test, answer, blank, tries)
  elif input == "medium" or input == "Medium":
    test = medium_test
    answer = medium_answers
    blank = blanks
    play_game(test, answer, blank, tries)
  elif input == "hard" or input == "Hard":
    test = hard_test
    answer = hard_answers
    blank = blanks
    play_game(test, answer, blank, tries)
  else:
    print "That is not a valid option!!"
    return game_level(level)

def play_game (test, answer, blank, tries):
  i = 0
  chances = 0

  print test

  while (i < len(answer)) and (chances < tries):
    guess = raw_input("What is your correct answer for " + blank[i] + "? ")
    if guess == answer[i]:
      print "That is correct!!"
      test = test.replace(blank[i], answer[i])
      print test
      i = i + 1
      if i == len(answer):
        print "Nice work! You've correctly filled in the blanks and won the game!"
    else:
       print "Sorry - that is incorrect. Please try again!! "
       chances = chances + 1
       if chances == tries:
         print "Sorry! You did not provide the correct answer. Thanks for playing."


game_level(raw_input)