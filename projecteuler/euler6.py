### 2019-01-03 mollyocr
#### projecteuler.net problem 6: sum square difference

## The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#### Make a list
one_hundred = range(1,101)
# print(list(one_hundred))

#### Find the squares and sum them up
squares = []

for i in one_hundred:
    squares.append(i*i)
    # print(f"i = {i}. Adding i*i {i*i} to the list...")

print(f"The list of squares 1-100 = {list(squares)}")

print(f"The sum of the squares 1-100 = {sum(squares)}")

#### Find the sum and square it
print(f"The sum of 1-100 = {sum(one_hundred)}")
print(f"The square of {sum(one_hundred)} = {sum(one_hundred) * sum(one_hundred)}")

#### Find the difference

print(f"The *absolute* difference between the sum_of_squares and square_of_sum = {abs(sum(squares) - (sum(one_hundred) * sum(one_hundred)))}")

#### The *absolute* difference between the sum_of_squares and square_of_sum = 25164150

#### Congratulations, the answer you gave to problem 6 is correct.
#### You are the 421916th person to have solved this problem.
