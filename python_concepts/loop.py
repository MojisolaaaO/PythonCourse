"""
A loop is a useful construct for when you would like to repeat the same actions
any number of times

For loops is useful when iterating over each item in a list
"""

fruits = ["apple", "mango", "pear", "cherry", "grapes"]

for i in fruits:
    print("Would you like {}?".format(i))


# the last number (10) will not be included in the output
for number in range(1, 10):
    print("Number {}".format(number))

# a while loop runs anytime a condition remains true

temp = 40
while temp > 32:
    print("The water is {} degrees.".format(temp))
    temp -= 1  # python decrement operator


"""
Loop controls 

break - ends the loop and goes to the next statement in the program
continue - skips the current part of the loop and moves to the next part 
pass - skips  any part of the loop where "pass" appears. best used for testing code
"""

grade = 95
while grade > 85:
    print("Your grade is {} %".format(grade))
    grade -= 1
    if grade == 90:
        break


for number in range(5, 15):
    if number == 8:
        print("We are skipping number 8")
        continue
    print("This is the number {}".format(number))


for number in range(5, 15):
    if number == 8:
        pass
    else:
        print("This is the number {}".format(number))


