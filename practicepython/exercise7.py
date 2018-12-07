### 2018-11-13 mollyocr
#### practicepython.org exercise 7: list comprehensions

## Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#### So here's the long way around just to get your feet wet after a week off.

# evens = []
#
# for i in a:
#     if i % 2 == 0:
#         evens.append(i)
#
# print (evens)

#### Ok but now do it in one line with a list comprehension, yo. That's the point of the exercise, duh.

# evens = [i for i in a if i % 2 == 0]
# print (evens)

print ([i for i in a if i % 2 == 0])
