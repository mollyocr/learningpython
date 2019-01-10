### 2019-01-04 mollyocr
#### practicepython.org exercise 20: element search

## Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

## Extra: Use binary search.

a = [1, 3, 5, 30, 42, 43, 500]

def get_input(help_text="I have a list of numbers. Give me a number, and I'll return TRUE or FALSE for whether or not your number is in my list. >> "):
    return (int(input(help_text)))

number_to_eval = get_input()

if number_to_eval in a:
    print(f"Yep, {number_to_eval} is in my list. ")
else:
    print(f"Nope, {number_to_eval} is not in my list. ")
