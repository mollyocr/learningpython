### 2018-12-06 mollyocr
#### practicepython.org exercise 12: list ends

## Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]

#### First pass. Really clunky.
# def list_lopper(list_name):
#     b = []
#     b.append(list_name[0])
#     b.append(list_name[-1])
#     print(f"Here is a new list consisting of only the first and last elements of the list provided: {b} ")
#
# list_lopper(a)

#### Second pass is slightly less clunky.

# def list_lopper(list_name):
#     b = [list_name[0], list_name[-1]]
#     print(b)
#
# list_lopper(a)

#### But after checking out the solution page -- holy cow this is so neat and tidy:

def list_lopper(list_name):
    return [list_name[0], list_name[-1]]

print(list_lopper(a))

#### This^ little thing of wrapping the function call inside of a print seems like a thing that happens a lot but it sure isn't intuitive to me.

#### ARGH, I still don't really get return, argh.
#### OH it's the ARGUMENT that goes INTO the print FUNCTION!
