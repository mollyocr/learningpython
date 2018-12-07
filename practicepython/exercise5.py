### 2018-10-29 mollyocr
#### practicepython.org exercise 5: list overlap

## Take two lists, say for example the two below, and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#### First stab -- but this doesn't dedupe the numbers and is dependent on the number of items in list a.

# c = []
#
# for number in a:
#     if number in b:
#         c.append(number)
#
# print (c)

#### OR

# for number in a:
#     if number in b:
#         print (number)

#### Second stab -- Went googling for "how to find common items in two lists python." Landed on set objects.
#### Non-operator will accept any iterable as an argument. The operator version requires that the arguments be sets.

# print ( set(a).intersection(set(b)) ) # operator version
# print (set(a) & set(b)) # non-operator version

#### Third stab -- Surely there's a way to kludge it together with just what's been gleaned from the exercies so far. Need a for/if something something but the logic is making my brain hurt.

## Randomly generate two lists to test this.

import random
# a = random.sample(range(1, 100), random.randint(1,100))
# b = random.sample(range(1, 100), random.randint(1,100))

#### random.randint(a,b) -- Return a random INTEGER N such that a <= N <= b.

#### DONE: I was using random.sample it doesn't have replacement (unique elements returned only), which isn't really random, is it?
    #### random.sample (population, k) -- Return a k length LIST of unique elements chosen from the population sequence or set.
    #### random.randrange(start, stop[, step]) -- Return a randomly selected element from range(start, stop, step). This is equivalent to choice(range(start, stop, step)), but doesn’t actually build a range object.
    #### random.choices(population, weights=None, *, cum_weights=None, k=1) -- Return a k sized list of elements chosen from the population with replacement.

#### Q: What's the difference between random.randint and random.randrange really?
#### A, probably: randint returns INTEGER; randrange could return ANY ELEMENT in a range.

a = random.choices(range(1, 100), k=random.randint(1,100))
b = random.choices(range(1, 100), k=random.randint(1,100))

#### Had to put the k= in this^ for it to work. Once you name a parameter, all parameters after it have to be named. It can parse the stuff that comes first.

# print (f"a = {a}")
# print (f"b = {b}")

#### Hey, good for you, applying fstrings, mf.
#### But omg I want those numbers in order in all the lists because they're ugly and it looks like fstrings can't take methods with their variables. That is,
    #### print (f"b = {b.sort()}")
    #### doesn't work.

#### SO... ???

# print ("b = " + str(b.sort())) #### NOPE. Getting "None" in place of list b. But list d of the numbers in common is working.
# print (str(b.sort())) #### NOPE. Getting "None" in place of list b. But list d of the numbers in common is working.
# print (b.sort()) #### NOPE. Getting "None" in place of list b. But list d of the numbers in common is working.

#### THEN I GOOGLED MORE. list.sort() METHOD will always return "None" to "avoid confusion." What I really want is the sorted() FUNCTION!

# print (sorted(a))
# print (sorted(b))

### Can I do this inside fstrings??

print (f"a = {sorted(a)}") #### YES!!
print (f"b = {sorted(b)}") #### HELL YES!!

c = a + b # AH HA!
d = []

for number in c:
    if (number in a) and (number in b) and (number not in d):
        d.append(number)

print (f"Numbers in common between a & b = {sorted(d)}")

#### There is an occasional error: ValueError("Sample larger than population or is negative")
    #### "If the sample size is larger than the population size, a ValueError is raised."
#### DONE: Prevent this from happening!
#### Choosing the right random was the fix!

## Write this in one line of Python.

# print (set(random.choices(range(1, 100), k=random.randint(1,100))) & set(random.choices(range(1, 100), k=random.randint(1,100)))
