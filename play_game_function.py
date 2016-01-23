easy_test = "My name is __1__. I was born in __2__, in __3__. I am presently __4__ years old."
easy_answers = ["Luis", "New Orleans", "1975", "40"]
blanks = ["__1__", "__2__", "__3__", "__4__"]

difficulty = raw_input("Please enter the level of difficulty: easy, medium, or hard: ")
tries = raw_input("Please enter the number of guesses you would like for each blank: ")
tries = int(tries)

def play_game (test, answer, blank):
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

play_game(easy_test, easy_answers, blanks)
