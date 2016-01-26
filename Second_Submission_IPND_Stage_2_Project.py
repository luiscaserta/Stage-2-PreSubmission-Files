#Here is my tests and answers for all three game levels.
#Blanks are the fill in the blanks that the user must replace, and it is the same for each test.
easy_test = "__1__ are lines of code that are ignored by the computer and exist as a means to make notes to yourself \
or other programmers about the code. Adding comments to your code can help __2__ your code when things go wrong by \
comparing what the comment claims the code should do with what it actually does. In Python, you can make a comment \
by typing the __3__ symbol. Everything written after the symbol on that line will be the comment. Programmers have guidelines \
about how to write comments so that they are descriptive but not obtrusive: \
1. Don't comment obvious code.\
2. Start functions with a comment.\
3. Keep commments up-to-date.  and \
4. __4__"

easy_answers = ["comments", "debug", "#", "be concise"]

medium_test = "According to one of the video's in this stage, the following is __1__  Guide to All Problems in the Galaxy:\
1.  Don't __2__!!\
2.  Determine the __3__?\
3.  Determine the outputs?\
4.  Solve the problem: Work through some examples by hand.\
a.  Consider systematically how a human solves the problem.\
b.  Create algorithm known as __4__.\
5.  Simple mechanical solution - Don't optimize prematurely! Simple and Correct.\
6.  Develop incrementally and test as we go."

medium_answers = ["Pythonista's", "panic", "inputs", "pseudocode"]

hard_test = "String vs List \
There are two main differences between lists and strings. A list can hold __1__ we want but in a string, the elements \
can only be characters. The second big difference is that lists support __2__. This means that we can change the value of a list\
after we've created it; it modifies the existing object. If this done with a string, the program produces an error. \
We create a list using __3__. The list can then be reassigned a new value or mutated by changing a value within that \
list. If we write two different ways of referring to the same object, it's called __4__. If an object is mutable, we must be \
cognitive of other variables that might refer to that same object."

hard_answers = ["anything", "mutation", "square brackets", "aliasing", ]

blanks = ["__1__", "__2__", "__3__", "__4__"]

def number_of_tries(tries):
  '''This is the function to determine the number of guesses the user want to make for each anser.
  input is a user defined integer
  output is the user defined integer'''
  #This is my code to validate the input of the user.  It only accepts a positive integer.  I thought of this because I kept getting
  #an occasional error after I was asking for number of times the user wanted to guess the correct answer.  I didn't panic, and "eventually"
  #I was able to figure it out.  I figured this out by searching on the internet, and I am most proud of this little bit of code!! =)
  while True:
    try:
      tries = int(raw_input("How many guesses would you like for each problem?  Please enter a positive integer: "))
    except ValueError:
      print "Sorry, I didn't understand. Input must be a positive integer"
      continue
    if tries <= 0:
      print "Sorry, your response must not be negative!!"
      continue
    else:
      break
  return tries



def game_level(level):
  '''This is my function to have the user determine what level he wants to play.  I use the user's raw input answer to select the
  corresponding test and answer set.
  inputs are.....
  outputs are....'''
  input = raw_input("Choose level of game to play (easy, medium, hard): ")
  print "You have chosen level " + input + "!!"
  
  number_of_tries(raw_input)
  
  if input in ["easy","Easy"]: 
    play_game(easy_test, easy_answers, blanks, tries)
  elif input in["medium", "Medium"]:
    play_game(medium_test, medium_answers, blanks, tries)
  elif input in ["hard", "Hard"]:
    play_game(hard_test, hard_answers, blanks, tries)
  else:
    print "That is not a valid option!!"
    return game_level(level)

def play_game (test, answer, blank, tries):
  '''This is my function using simple while loop that sets the conditions for user to answer the fill in the blank test in accordance their own criteria.
  The variable i represents the blanks that must be filled in each test.  Once all blanks filled correctly, while loop ends.
  Chances is the variable that starts at 0 and must be less than tries to allow the game to continue.  If equal to user input tries
  it will end the game according to the instructions.
  inputs are......
  outputs are..........'''
  i = 0
  chances = 0

  print test

  while (i < len(answer)) and (chances < tries):
    guess = raw_input("What is your correct answer for " + blank[i] + "? ")
    if guess == answer[i]:
      print "That is correct!!"
      print
      test = test.replace(blank[i], answer[i])
      print test
      print
      i = i + 1
      if i == len(answer):
        print "Nice work! You've correctly filled in the blanks and won the game!"
    else:
       chances = chances + 1
       if chances == tries:
         print "Sorry! You did not provide the correct answer. Thanks for playing."
       else:
         print "Sorry - that is incorrect. Please try again!!"
         print

#This is how I start the game
game_level(raw_input)
