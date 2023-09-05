### Setup Section ###

from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if (letter in actual):
      

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == actual[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:
        
# ...so we'll print it out with a yellow background
        printColorfulLetter(letter,True,False)
  

    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      printColorfulLetter(letter,False,False)

    
    print(Style.RESET_ALL + " ", end="")

#Write a Function that takes in a six-lettered word from the user
def getSixLetterInput():
  option = ""
  #While word length is not equal to 6...
  while(len(option) != 6):
    #Keep prompting user for input
    option = input("Enter a 6 letter word: ")

  return option
  


### Main Program ###
#Write the logic of the game here!

#ASCII Art
print(r"""
 
 __    __                 _     ___                        
/ / /\ \ \ ___   _ __  __| |   / _ \ _   _   ___  ___  ___ 
\ \/  \/ // _ \ | '__|/ _` |  / /_\/| | | | / _ \/ __|/ __|
 \  /\  /| (_) || |  | (_| | / /_\\ | |_| ||  __/\__ \\__ \
  \/  \/  \___/ |_|   \__,_| \____/  \__,_| \___||___/|___/
                                                           
                                              """)

#Welcome user and explain instructions
print("······················")
print("Welcome to Word Guess!")
print("······················")

print("You have 5 tries to guess the word.")
print("The word is 6 characters long, and your guess MUST have 6 characters.")
print()
print("INSTRUCTIONS:")
print("-------------")
print("If a letter is RED, it is NOT in the word.")
print("If a letter is YELLOW, it is in the word but in the wrong location.")
print("If a letter is GREEN, it is the right letter in the right place.")
print()

correctWord = "eagles" #Answer to the game
guess = "" #Dummy variable
guessNum = 0 #Counter variable

#Repeat turn UNTIL user runs out of tries (6) or user guesses correctly
while((guess!= correctWord) and (guessNum < 6)):
  guess = getSixLetterInput()
  printGuessAccuracy(guess,correctWord)
  print()
  guessNum += 1


#Tell user whether they won or lost
if (guess == correctWord):
  print("You win!")
else:
  print("You lose this time!")
  