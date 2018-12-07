#### 2018-10-23 mollyocr
#### practicepython.org exercise 1: character input

## Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Hi! What's your name? ")
print("Nice to meet you, " + name + "!")

age = int(input("How old are you? "))
print(str(age) + ", huh? Still young.")

desiredage = int(input("How old do you want to be when you die? "))

import datetime
now = datetime.datetime.now()

deathyear = str((now.year - age)+desiredage)
print("You've got a lot of life yet to live. You won't be " + str(desiredage) + " years old until " + deathyear + ".")

## Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
## Print out that many copies of the previous message on separate lines.

# yearsleft = desiredage - age
#
# emphatic_message = ("You've only got " + str(yearsleft) + " years left until you're " + str(desiredage) + "! Get living! \n")
# print (emphatic_message)
#
# times_to_repeat = int(input("How many times should I shout this at you? "))
# print ((emphatic_message) * (times_to_repeat-1))

#### Personal challenge: Print -last- emphatic_message in ALL CAPS for added emphasis.
##???## How do I get rid of the extra line break between the repeating print and the ALL CAPS emphatic_message?
# print (emphatic_message.upper())

#### Personal challenage: Futureproof this with imported year.
#### >> Added datetime import and used now variable in place of 2018.

#### fstrings mean you don't have to do stupic concatenation stuffs with str

yearsleft = desiredage - age

emphatic_message = f"You've only got {yearsleft} years left until you're {desiredage}! Get living! \n"
print (emphatic_message)

times_to_repeat = int(input("How many times should I shout this at you? ")
print ((emphatic_message) * (times_to_repeat-1))
print (emphatic_message.upper())
