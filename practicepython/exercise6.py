### 2018-10-29 mollyocr
#### practicepython.org exercise 6: string lists

## Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

string_to_eval = input("Hi! Enter a string. I'll tell you if it's a palidrome or not. ")
#### Yo, you don't have to cast a str because input is always a string.
string_to_eval = string_to_eval.replace(" ", "")

#### list[start, stop, step] will build you a sublist.
# string_backwards = string_to_eval[::-1]
#
# if string_to_eval == string_backwards:
#     print (f"\"{string_to_eval}\" is a palindrome!")
# else:
#     print (f"\"{string_to_eval}\" is not a palindrome!")

#### You can condense it tho:

if string_to_eval == string_to_eval[::-1]:
    print (f"\"{string_to_eval}\" is a palindrome!")
else:
    print (f"\"{string_to_eval}\" is not a palindrome!")

#### DONE: This only works for palindromes that are words, not phrases with spaces. Fix that! How do you erase spaces?
#### Print lines aren't pretty anymore.
