### 2018-12-14 mollyocr
#### projecteuler.net problem 5: smallest multiple

## 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

## What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#### So you need to build a function that will % some integers and spit out the lowest one

#### What are some things I know about the number?
# It's positive
# It's even
# It's > 20
# It's a multiple of 20
# It's a multiple of 2520!

#### So I can increment by 2520 inside of a loop then spit out the first one I get back.

def modularizer():
    candidate = 2520 # Start here
    while 1 == 1: # This still feels hacky. I just mean "keep doing this" until...
        candidate += 2520 # Step
        if candidate % 11 == 0 and candidate % 12 == 0 and candidate % 13 == 0 and candidate % 14 == 0 and candidate % 15 == 0 and candidate % 16 == 0 and candidate % 17 == 0 and candidate % 18 == 0 and candidate % 19 == 0: # Every condition must be satisfied
            return candidate # Spit it out
            break # Bail! I only need the first one

print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {modularizer()}.")

#### The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is 232792560.
#### Congratulations, the answer you gave to problem 5 is correct.
#### You are the 416706th person to have solved this problem.
