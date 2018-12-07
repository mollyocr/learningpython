### 2018-12-06 mollyocr
#### Safari Books Online: Learn Python 3 - Exercise 20

# Go through the script and type a comment above each line explaining in English what it does.

#### This defines the function cheese_and_crackers that takes two arguments: cheese_count and boxes_of_crackers.
def cheese_and_crackers(cheese_count, boxes_of_crackers):

  #### This prints an fstring that includes the first arguments of the function cheese_and_crackers, cheese_count.
  print(f"You have {cheese_count} cheeses!")

  #### This prints an fstring that includes the second arguments of the function cheese_and_crackers, boxes_of_crackers.
  print(f"You have {boxes_of_crackers} boxes of crackers!")

  #### This prints some more stuff. ALL OF THIS is included inside the function, so anytime cheese_and_crackers is called, this cute shit comes with it.
  print("Man that's enough for a party!")
  print("Get a blanket.\n")

print("We can just give the function numbers directly:")
#### This calls the function cheese_and_crackers and provides values for the two arguments it takes, cheese_count and boxes_of_crackers.
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
#### This declares and assigns values to two new script-level variables, amount_of_cheese and amount_of_crackers. These two variables don't yet have anything to do with the cheese_and_crackers function.
amount_of_cheese = 10
amount_of_crackers = 50

#### This calls the function cheese_and_crackers and provides the two new variables declared above as its two arguments. When calling the cheese_and_crackers function this way,
    #### cheese_count = amount_of_cheese
    #### boxes_of_crackers = amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
#### This calls the cheese_and_crackers function but puts provides as its arguments two equations that have to be mathed.
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
#### Here, the two variables provided as arguments to the function are being changed on their way into the function with some maths.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
