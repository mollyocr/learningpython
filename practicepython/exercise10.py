### 2018-11-28 mollyocr
#### practicepython.org exercise 10: list overlap comprehensions

## This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

## Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
## and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

## The original formulation of this exercise said to write the solution using one line of Python, but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed on the blog, so you can either choose to use the original directive and read about the set command in Python 3.3, or try to implement this on your own and use at least one list comprehension in the solution.

## Extra: Randomly generate two lists to test this

#### Here's the randomly generated lists
# a = random.choices(range(1, 100), k=random.randint(1,100))
# b = random.choices(range(1, 100), k=random.randint(1,100))

#### Yeah so I did all this already, at least one way.

# c = a + b
# d = []
#
# for number in c:
#     if (number in a) and (number in b) and (number not in d):
#         d.append(number)
#
# print(d)

#### But this isn't a list comprehension, so here's another go.

# print ([i for i in (a + b) if i in a and i in b]) # Doesn't exclude duplicates.

# d = []
# d = [i for i in (a + b) if (i in a) and (i in b) and (i not in d)] # Still has duplicates. This doesn't work because it's not... sequential like a for loop is even though it sort of iterates. Like, parallel-processing.)
# print(d)

#### This has a list comprehension and pulls out the duplicates with a set -

# d = set([i for i in (a + b) if (i in a) and (i in b)])
# print(d)

#### Or move the set and skip the concatenation
#### mike.allen > you can do list comprehension on a list that was created from a set

d = [i for i in set(a) if (i in b)]
print(d)

#### but the instructions are all about how complicated list comprehensions can be so I think there should be some way to do it without sets, just 'cause.

# d = [i for i in (a+b) if (i in a) and (i in b)] # Still has duplicates.
# print(d)
#
# e = [i for i in d if d.count(i) > 1] # This doesn't work, yo. GOTTA SET THEM SETS.
# print(e)

#### Here's the ONE-LINE version using random lists of random numbers and SETS
# print (set(random.choices(range(1, 100), k=random.randint(1,100))) & set(random.choices(range(1, 100), k=random.randint(1,100)))
