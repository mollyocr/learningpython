### 2018-12-13 mollyocr
#### practicepython.org exercise 16: password generator

## Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

#### QUESTION: wtf does this mean? "Include your run-time code in a main method."

## Extra: Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

#### Well I'll fersure need this
import random

#### Then what? Brainstorm:
# Need input for how weak/strong to make the pw.
# Maybe weak = two random words from a word list. Fun!
# Strong = Need more input for how long user wants the pw to be, then random number generation.
# I don't need random ints though, I need random chars -- strings...
# Oh! Ask and google shall provide:
import string

#### This again
def get_string(help_text="Please provide a string: "):
    return str(input(help_text))

def get_integer(help_text="Provide a number: "):
    return int(input(help_text))

### Now let's make a randomish pw that I can remember
def weak_pw_gen(weak_plz):

    adjectives = ["Angry", "Beautiful", "Clever", "Dangerous", "Exciting", "Forgetful", "Graceful", "Happy", "Inconsiderate", "Lucky", "Old", "Pretty", "Romantic", "Sad", "Ugly"]

    animals = ["Alligator", "Bear", "Chicken", "Duck", "Elephant", "Fox", "Giraffe", "Horse", "Iguana", "Kangaroo", "Lion", "Monkey", "Octopus", "Panda", "Rabbit", "Snake", "Tiger", "Wolf", "Zebra"]

    pw_front = random.choices(adjectives)
    pw_back = random.choices(animals)

    print(f"adj = {pw_front}")
    print(f"animal = {pw_back}")

    pw = pw_front[0] + pw_back[0]

    # print(f"Your pw is {str(pw)}, but like put together ARGH")

    return pw

#### Make it run
# print(weak_pw_gen(get_string("Would you like a weak pw? Enter y >> ")))

#### ARGH, I can't figure out how to join/concatenate the two parts all pretty-like and it's driving me BONKERS. join function doesn't work here because it'll only take two things from the same list/set. DONE: Work this out with Mike.

#### Try again but simpler so you can make it work on your own.
def weak_pw_gen_v2(weak_plz):

    things = ["Capricorn", "Android", "Dragon", "Martian", "Mermaid", "Ogre", "Phoenix", "Robot", "Sphinx", "Spirit", "Unicorn", "Vampire", "Werewolf"]

    pw = "".join(random.sample(things, k=2)) # Using random.sample because I didn't like "DragonDragon" as a pw

    # print(f"Your pw is {str(pw)}, but like put together ARGH")

    return pw

#### Fine. Cool. Now let's make a stronger pw generator.
def strong_pw_gen(strong_plz):

    length = get_integer("How many characters do you need your strong password to be? Please enter an integer >> ")

    characters = string.ascii_letters + string.digits + string.punctuation
    #### TODO: Try this! How else can you do this? "chr()" function + random ints

    pw = "".join(random.choices(characters, k=length)) # Using random.choices here bc replacement is randomer

    return pw

#### Make it run
pw_type = get_string("What type of password would you like? Please enter \"weak\" or \"strong\" >> ")

if pw_type == "weak":
    print(f"Here is your weak (rememberable) password: {weak_pw_gen_v2(pw_type)}")
    # print(f"Here is your weak (rememberable) password: {weak_pw_gen(pw_type)}")
elif pw_type == "strong":
    print(f"Here is your strong password: {strong_pw_gen(pw_type)}")
else:
    while pw_type != "weak" or "strong":
        print(f"Huh? I don't understand. ")
        pw_type = get_string("What type of password would you like? Please enter \"weak\" or \"strong\" >> ")
        if pw_type == "weak":
            print(f"Here is your weak (rememberable) password: {weak_pw_gen_v2(pw_type)}")
            # print(f"Here is your weak (rememberable) password: {weak_pw_gen(pw_type)}")
            break
        elif pw_type == "strong":
            print(f"Here is your strong password: {strong_pw_gen(pw_type)}")
            break

# TODO: Rework with secrets modle instead of random bc security.
# TODO: Find a pylint (find the missing brackets etc) package for Atom.
# TODO: pycharm??
