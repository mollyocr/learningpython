#### 2018-10-25 mollyocr
#### practicepython.org exercise 4: divisors

## Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (A divisor is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

number_to_eval = int(input("Hi! Enter a number, and then I'll tell you all of its divisors. "))
#### Good job, yo, for casting that input up front.

##### 1. take number_to_eval & create a list using range function of all of the integers between 0 and number_to_eval... plus the number_to_eval itself

eval_range = range(1, number_to_eval+1)
# print (list(eval_range))

#### A number is a divisor of itself so the +1 is necessary to include number_to_eval in the range. Is there a more elegant way to do this?
#### Similarly, need to exclude 0 from the range or you'll get a "ZeroDivisionError: integer division or modulo by zero" error.

##### 2. you'll need some for and if statements, and another list to put things in

# divisor_list = []
#
# for item in eval_range:
#     if number_to_eval % item == 0:
#         divisor_list.append(item)
#
# print (divisor_list)

#### OR you can just print it. Cleaner but not as portable maybe?--

for item in eval_range:
    if number_to_eval % item == 0:
        print (item)
