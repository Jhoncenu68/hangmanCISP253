#!bin/bash
# Davenport University
# Class CISP 253 (Fall 2023)
# Author: AJ Sanchez
# Program Name: asanchez21_midterm__hangman.py

# The Doc string description of the program
"""
This is the midterm for CISP253 Which is a hangman game that uses turtle as an interface for the user to interact with and random to randomly select from the list of words in the wordbank.
"""
from turtle import *
# using  from turtle import * simply becuase i dont want to have to put turtle. infront of every command just to save time
import random

# This is the series of code that handles all of the drawing of the stickman when guessing incorrectly
# The drawMan variable is used later in the code to determine what part of the body part to draw according to x Ex: drawMan(1) would be the first guess and would draw the head
def drawMan(x):
    guess = x
    if guess == 1: 
        # Draws the head of the stickman
        goto(-74, 140)
        pendown()
        right(90)
        circle(15,None,100)
        penup()
    elif guess == 2:
        # Draws the torso of the stickman
        goto(-74, 140)
        pendown()
        left(90)
        penup()
        forward(30)
        pendown()
        forward(40)
        right(180)
        forward(30)
        penup()
    elif guess == 3:
        # Draws the stickmans Left arm
        goto(-74, 100)
        pendown()
        left(55)
        forward(45)
        right(180)
        forward(45)
        penup()
    elif guess == 4:
        # Draws the stickmans Right Arm
        goto(-74, 100)
        pendown()
        left(70)
        forward(45)
        right(180)
        forward(45)
        penup()
    elif guess == 5:
        # Draws the stickmans left leg
        goto(-74, 100)
        pendown()
        left(55)
        forward(30)
        right(30)
        forward(60)
        right(180)
        forward(60)
        penup()
    elif guess == 6:
        # Draws the stickmans right leg which is the final guess
        goto(-74, 70)
        pendown()
        right(120)
        forward(60)
        penup()

# This configures turtle to not show the cursor, set the drawing speed to max and change the thickness of the pen
hideturtle()
speed(0)
pensize(2)

# The word bank used for the game that will be randomly choosen.  I could have definitly added more words using a seperate wordlist document but this was the way I knew how to best impliment a wordlist.
words = ('funny','galaxy','lucky','matrix','linux',
            'faking','jinx','staff','yoked','unknown',
            'equip','subway','kiosk','fixable','fjord',
            'galvanize','khaki','quiz','kilobyte','megahertz',
            'terrabyte','cobweb','jelly','rhubarb','quartz',
            'quips','kazoo','klutz','fox','numbskull')

# The bored variable is used to determine if the game is actually being played.  See line 162 where it is being used to determine the game is done and the user has quit
bored = False
# this is basically the command that will run all the code once it has determined that bored is false.
while not bored:

    # Draws the base thingy not sure the technical term.  Post maybe?
    home()
    pendown()
    left(90)
    forward(175)
    left(90)
    forward(74)
    left(90)
    forward(35)
    penup()
    goto(-135,-35)
    
    # Uses the random library to chose a random word from the listed wordbank
    word = random.choice(words)

    # This draws the amount of bars of however many letters are in each word using  courier font in 14 point size
    for i in word:
        write('_ ', True, font=("Courier", 14, "normal"))
    
    correct = []
    wrong = 0
    terminate = False
    # This while command is basically determining if you have failed based on the amount of guesses that are wrong
    while wrong < 6 and not terminate:
        # This is the window pox that pops up allowing  you to guess your letter
        # The go to command also sets the turtle cursor to where the head would be drawn
        letter = textinput('Hangman','Guess a letter in lowercase:')
        goto(-135,-35)
        if letter not in correct:
            for i in word:
                if i == letter:
                    write(letter.upper() + ' ', True, font=("Courier", 14, "normal"))
                    correct += letter
                else:
                    write('_ ', True, font=("Courier", 14, "normal"))
        # This small string is determining if the letter you guessed is in the word or not.  If its not in the word it will add 1 to the current drawMan(x) variable until it reaches 6
        if letter not in word:
            wrong += 1
            drawMan(wrong)
        # This entire string of code is the process for the fail screen so if the amount wrong is = to 6 it will pop up a window saying "Sorry, you lose!"
        if wrong == 6:
            goto(-135,-35)
            for i in word:
                if i in correct:
                    write('_ ', True, font=("Courier", 14, "normal"))
                else:
                    write(i.upper() + ' ', True, font=("Courier", 14, "normal"))
            goto(-74, -60)
            write('Sorry, you lose!', False, align='center', font=("Courier", 14, "normal"))
        # This is the string of code that pops up the win screen if you guess correctly
        if len(correct) == len(word):
            goto(-74, -60)
            write('Congratulations!', False, align='center', font=("Courier", 14, "normal"))
            terminate = True

    # This brings up a window asking  if the user wants to replay.
    response = textinput('Hangman','Would you like to play again? (y or n): ')
    # This brings up a confirmation screen to confirm if the user wants to quit
    while response != 'y' and response != 'n':
        response = textinput('Hangman','Please enter "y" or "n": ')
    #  y makes it so the user cancels closing the game
    if response == 'y':
        clear()
    # n makes it so the user who is closing the game closes the game and clears the screen and returns the cursor to (0, 0)
    elif response == 'n':
        clear()
        home()
        # Turtle will write a message thanking the user for playing.
        write('Thanks for playing!', False, align='center', font=("Courier", 25, "normal")) 
        bored = True
        
# Professor if you are reading this I only put these here becuase I am posting this code on github just incase I need to come back to it as a refresher.  THERE IS NO CODE BEYOND THIS POINT!!!!

# If you are reading these end comments I only really talk about any issues I had while making this or any issues in the program I couldn't fix
# A current issue with the code is that when you press cancel on any text box it creates an error and freezes the program.  Not sure how to fix this and due to this being a project just for school I dont think I will come back to it unless I'm Really bored
# Another issue is when you press 'n' when closing the game it doesnt actually stop the program it just comes up with a the thanks for playing screen.  The user still manually needs to stop the backend.  This most likely  also wont be fixed for the same reason listed above
# This is probably just becuase I am a amaetur at this programming stuff I couldnt figure out how to actually implement a seperate wordlist file and import it into the code.  So I just ended up using random to select from a big wordlist which was turned into a variable.
# I have a feeling  this is pretty much the same thing I would imagine implementing a seperate wordlist file would work but becuase I did it this way I am limited to how many possible words there are due to the fact I dont want it to take up 50+ lines of variables
# Other than that was the only real issues I had.  I learned alot about turtle in this project becuase after some hours of research I learned you can use text boxes
# I also learned that turtle can draw letters...  I had no idea it could do this and have been drawing all letters with seperate commands in the past *face palm*