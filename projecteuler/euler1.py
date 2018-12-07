### 2018-10-29 mollyocr
#### projecteuler.net problem 1: multiples of 3 and 5

## If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
## Find the sum of all the multiples of 3 or 5 below 1000.

#### Honestly, this is mostly just a copy/paste job!

number_to_eval = int(input("Hi! What number would you like me to evaluate? I'll tell you the sum of all the multiples of 3 or 5 that are less than that number. "))

eval_range = range(1, number_to_eval)
multiple_list = []

# for i in range(0, len(eval_range)): # For each thing in the range of the index of the list up to the total number of things in the list...
#     if eval_range[i] % 5 == 0:
#         multiple_list.append(eval_range[i])
#     elif eval_range[i] % 3 == 0:
#         multiple_list.append(eval_range[i])
    #### Do I have to have an else statement?

for i in range(0, len(eval_range)): # For each thing in the range of the index of the list up to the total number of things in the list...
    if eval_range[i] % 5 == 0 or eval_range[i] % 3 == 0:
        multiple_list.append(eval_range[i])

print (f"List of all multiples of 3 or 5 below {number_to_eval}: {multiple_list}")
print (f"Sum of all multiples of 3 or 5 below {number_to_eval}: {sum(multiple_list)}")

#### When number_to_eval = 1000, the sum of all the multiples of 3 or 5 below it is 233168.
#### Congratulations, the answer you gave to problem 1 is correct.
#### You are the 793646th person to have solved this problem.
