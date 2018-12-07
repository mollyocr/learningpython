### 2018-10-29 mollyocr
#### projecteuler.net problem 3: largest prime factor

## The prime factors of 13195 are 5, 7, 13 and 29.
## What is the largest prime factor of the number 600851475143 ?

small = 13195
big = 60851475143
toggle = big

#### Cool, so this list works, but now I have to figure out how to build this list of primes since it's obviously not complete or calculable.
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

primes = []

#### So you have to be able to nest for loops, right??

# for number_to_eval in range(2,toggle+1):
#
#     for j in range(2, number_to_eval):
#         if number_to_eval % j == 0:
#             print (f"{j} is not a prime.")
#         else:
#             primes.append(number_to_eval)

#### OH GOD NO, it keeps spinning numbers FOREVER.
#### Need a BREAK out of the loop. Cribbing off of https://hackernoon.com/prime-numbers-using-python-824ff4b3ea19 but playing along through each of the methods irl to feel the burn.

# for number_to_eval in range(2,toggle+1):
#     isPrime = True
#     for j in range(2, number_to_eval):
#         if number_to_eval % j == 0:
#             isPrime = False
#             print (f"{number_to_eval} is not prime.")
#             break
#     if isPrime:
#         print (f"{number_to_eval} is prime. Adding to list...")
#         primes.append(number_to_eval)

#### THIS IS STILL TAKING WAY TOO LONG, so here's the square root bit added in:
#### I sort of understand the why of this, but frankly I'm pushing through a little because primes are an UNUSUAL BEAST that I hope to encounter infrequently.

# for number_to_eval in range(2,toggle+1):
#     isPrime = True
#     for j in range(2, int(number_to_eval**0.5)+1):
#         if number_to_eval % j == 0:
#             isPrime = False
#             print (f"{number_to_eval} is not prime.")
#             break
#
    # if isPrime:
    #     print (f"{number_to_eval} is prime. Adding to list...")
    #     primes.append(number_to_eval)

# special_list = range(2,toggle+1)
#
# for number_to_eval in special_list:
#     isPrime = True
#     for j in range(2, int(number_to_eval**0.5)+1):
#         if number_to_eval % j == 0:
#             isPrime = False
#             print (f"{number_to_eval} is not prime.")
#             break
#
#     if isPrime:
#         print (f"{number_to_eval} is prime. Adding to list...")
#         primes.append(number_to_eval)

primes = [2, 3,5]
print (primes)

# j=2
# while len(primes) == 0:
#     toggle = toggle-1
#     if toggle % j != 0:
#         primes.append(toggle)

#### TODO: Google some pretty little short algorithm that tells you if a number is prime. Then stick it in this while loop somehow.

#### This is still taking a looooong time but I think going faster.

#### Here's a super short version I stole from here: http://code.activestate.com/recipes/162479-generating-a-list-of-prime-numbers-in-one-statemen/
# primes = [p for p in range(2,toggle) if not [0 for d in range(2,p) if p%d==0]]

#### TODO: Parse this^ shit.

# print (f"Here's your list of applicable primes: {primes}")

prime_factors = []

for i in range(0, len(primes)): # For each thing in the range of the index of the list up to the total number of things in the list...
    if toggle % primes[i] == 0:
        print (f"Found a prime factor: {primes[i]}. Adding it to the list...")
        prime_factors.append(primes[i])

print (f"Here's a list of all the prime factors of {toggle}: {prime_factors}")
print (f"This one is the largest prime factor: {prime_factors[-1]}")

#### The largest prime factor of 600851475143 is: 6857
#### Congratulations, the answer you gave to problem 3 is correct.
#### You are the 454746th person to have solved this problem.
