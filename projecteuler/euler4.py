### 2018-11-16 mollyocr
#### projecteuler.net problem 4: largest palindrome product

## A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
## Find the largest palindrome made from the product of two 3-digit numbers.

#### Two approaches come to mind right away:
    #### 1. Make two lists of three digits numbers, then list comprehension multiply them + palindrome check
    #### 2. Find the largest between the range of the products of 100*100 and 999*999 then factor it!

#### Approach 1

#### Make two lists of three digit numbers
a = list(range(100, 1000))
b = list(range(100, 1000))

#### Here are some baby lists for testing toggling.
# a = [100, 101, 102]
# b = [100, 101, 102]

#### List comprehension multiply the lists into a list of products

def multiplier(list_a, list_b):

    products = []

    for i in a:
        for j in b:
            products.append(i * j)
            # print(f"Appending product of {i}*{j} to list of products")
    return set(products)

products = multiplier(a, b) # I'm reusing a list name outside of the function which isn't ideal but here makes sense; is there a cleaner way to "export" it instead of double-scoping?

# print(f"Products: {products}") # The PRINTING is the part of ALL THIS maths that takes time. Computers are cool.


#### Palindrome checker

def pal_check(products_list): # highest_pal_returner

    palindromes = []

    for k in products_list:
        if str(k) == str(k)[::-1] and len(str(k)) > 3:
            palindromes.append(k)
            # print(f"Appending palindrome {k} to list")

    return max(set(palindromes)) # jfc I feel so smart. I NOW GET WHY FUNCTIONS ARE GREAT. Here, the function is a shoebox for all the ugly stuff, and allllllll I care about is that one sweet little morsel that comes out of the shoebox.

print(f"Here's the largest palindrome product of two 3-digit numbers: {pal_check(products)}")

#### The largest palindrome made from the product of two 3-digit numbers is 906609.
#### Congratulations, the answer you gave to problem 4 is correct.
#### You are the 408414th person to have solved this problem.

#### HOW TO TIME STUFF
import time
start_nanos = time.perf_counter_ns()
elapsed_time = start_nanos - time.perf_counter_ns()
