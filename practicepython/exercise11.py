### 2018-11-28 mollyocr
#### practicepython.org exercise 11: check primality functions

## Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

#### Yay, reusable bones!

def get_integer(help_text="Provide a number: "):
    return int(input(help_text))

#### Define some variables you'll need.

number_to_eval = get_integer("Hi! Enter a number, and then I'll tell you if it's prime. ")

eval_range = range(2, (number_to_eval//2)+1)
print (list(eval_range))

####

should_run = None

#### Let's build a prime_checker reusable bone!

def prime_checker(number_to_eval):

    print(f"We're assessing this number: {number_to_eval} ")

    if number_to_eval < 2:
        is_prime = False

    elif number_to_eval == 2:
        is_prime = True

    else:
        print("Elsing. ")

        for i in eval_range:
            print(f"Checking factors, i = {i}")
            if number_to_eval % i == 0:
                is_prime = False
                # break
            else:
                is_prime = True
                # break

        if is_prime:
            print (f"{number_to_eval} is prime.")
        elif is_prime == False:
            print (f"{number_to_eval} is not prime.")

    print(f"Almost done. is_prime = {is_prime}")

    return is_prime

#### Now make it run with a something, I guess?!

while should_run == None:
    print(f"Firing up. ")
    should_run = prime_checker(number_to_eval)
