#### 2018-10-23 mollyocr
#### practicepython.org exercise 3: list less than ten

## Take a list and write a program that prints out all the elements of the list that are less than 5.

number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for item in number_list:
#     if int(item) < 5:
#         print (item)

## Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.

# new_list = []

# for item in number_list:
#     if int(item) < 5:
#         new_list.append(item)
#
# print (new_list)

### Write this in one line of Python.

#### New thing is needed! A "list comprehension" -- http://blog.cdleary.com/2010/04/learning-python-by-example-list-comprehensions/

# new_list = [item for item in number_list if item < 5]
# print (new_list)

# print ([item for item in number_list if item < 5])

## Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

new_list = []

threshold = input("Hi. I have a list of numbers. I'll return all the numbers in my list that are less than the threshold you specify. What's the threshold? ")

# for item in number_list:
#     if int(item) < int(threshold):
#         new_list.append(item)
#
# print (new_list)

#### Specifying an item in the list with indexing. Index starts at 0.
# print (number_list[6])

for i in range(0, len(number_list)): # For each thing in the range of the index of the list up to the total number of things in the list...
    if int(number_list[i]) < int(threshold):
        new_list.append(number_list[i])

print (new_list)

#### Python has tidy for loops but other langages don't so this form is a lot more common
