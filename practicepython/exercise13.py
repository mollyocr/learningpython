### 2018-12-06 mollyocr
#### practicepython.org exercise 13: fibonacci

## Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

#### TODO:
    #### 1. Define a function fib_gen that takes one argument that is user input.
    #### 2. Do some stuff inside the fib_gen function to generate Fibonacci numbers.

#### Reuse this bit!
def get_integer(help_text="Provide a number: "):
    return int(input(help_text))

#### Here's the sauce
# def fib_gen(seq_len):
#
#     #### Declare a bunch of stuff
#     n1 = 1
#     n2 = 1
#     nth = n1 + n2
#     fib_list = [n1, n2]
#
#     #### Do stuff with it
#     while len(fib_list) < seq_len:
#         nth = n1 + n2
#         fib_list.append(nth)
#         n1 = n2
#         n2 = nth
#
#     return fib_list
#
# print(fib_gen(get_integer("Provide a number and I'll give you back that many Fibonacci numbers. ")))

#### This function looks long, but this flowed easily!

#### Ah, peeked at the solution, and I didn't account for int input <2. And there's some more elegance to steal around nth-ing. So --
def fib_gen(seq_len):

    #### Declare stuff
    n = 1

    #### if
    if seq_len == 0:
        fib_list = []
        return # BAIL OUT on the rest of this function because it doesn't need to go any further x all

    elif seq_len == 1:
        fib_list = [1]

    elif seq_len == 2:
        fib_list = [1, 1]

    elif seq_len > 2:
        fib_list = [1, 1]

        while len(fib_list) < seq_len:
            # These next two lines are the good stuff. Not as at-a-glance me-parsable but neater than the n1 & n2 variables I was lugging around.
            fib_list.append(fib_list[n] + fib_list[n-1])
            n += 1

    return fib_list

print(fib_gen(get_integer("Provide a number and I'll give you back that many Fibonacci numbers. ")))
