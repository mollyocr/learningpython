#### 2018-10-23 mollyocr
#### practicepython.org exercise 2: odd or even

## Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

# number_to_eval = input("Hi! What number would you like me to evaluate? For now, I'll tell you if the number provided is EVEN or ODD. ")
#
# if int(number_to_eval) % 2 == 0:
#     print ("The number you provided (" + str(number_to_eval) + ") is EVEN.")
# else:
#     print ("The number you provided (" + str(number_to_eval) + ") is ODD.")

## If the number is a multiple of 4, print out a different message.

# number_to_eval = input("Hi! What number would you like me to evaluate? I'll tell you if the number provided is EVEN or ODD - and if it happens to be a multiple of 4. ")
#
# if int(number_to_eval) % 4 == 0:
#     print ("The number you provided (" + str(number_to_eval) + ") is EVEN and is a multiple of 4.")
# elif int(number_to_eval) % 2 == 0:
#     print ("The number you provided (" + str(number_to_eval) + ") is EVEN.")
# else:
#     print ("The number you provided (" + str(number_to_eval) + ") is ODD.")

## Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number_to_eval = int(input("Hi! What number would you like me to evaluate?" ))
denominator = int(input("What would you like me to use as the denominator?" ))

#### Good idea to cast for input ^^^

if int(number_to_eval) % int(denominator) == 0:
    print ("The denominator (" + str(denominator) + ") divides evenly into the number you provided (" + str(number_to_eval) + "). ")
else:
    print ("The denominator (" + str(denominator) + ") does NOT divide evenly into the number you provided (" + str(number_to_eval) + "). ")

#### You can leave out the str "cast" in the concatenated string because it's already in a string but like nbd being explicit
