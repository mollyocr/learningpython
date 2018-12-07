### 2018-12-06 mollyocr
#### practicepython.org exercise 14: list remove duplicates

## Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

    ## Write two different functions to do this - one using a loop and constructing a list, and another using sets.

    ## Go back and do Exercise 5 using sets, and write the solution for that in a different function.

import random
a = random.choices(range(1, 100), k=random.randint(1,100))

#### Here's the easy peasy sets version of the function.
def set_maker(list_name):
    return set(list_name)

print(f"Here's the raw list with **{len(a)}** elements:  \n{a}")
print(f"Here's the SET with **{len(set_maker(a))}** elements:  \n{set_maker(a)}") # The function call is just BURIED in here.

#### Here's the loop version
# def set_maker(list_name):
#     b = []
#     for i in a:
#         if i not in b:
#             b.append(i)
#     return b
#
# print(f"Here's the raw list with **{len(a)}** elements:  \n{a}")
# print(f"Here's the deduped LIST with **{len(set_maker(a))}** elements:  \n{sorted(set_maker(a))}") # Added sorted because it's prettier.
