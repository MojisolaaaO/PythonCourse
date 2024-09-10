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
continue - skips the current part of the loop and moves to the next part of the loop 
pass - skips any part of the loop where "pass" appears. best used for testing code
"""

grade = 95  # Initialize the variable 'grade' with a value of 95

while grade > 85:  # Start a loop that runs as long as 'grade' is greater than 85
    print("Your grade is {} %".format(grade))  # Print the current value of 'grade'

    grade -= 1  # Decrease the value of 'grade' by 1 on each iteration (grade = grade - 1)

    if grade == 90:  # If 'grade' reaches 90, exit the loop
        break


for number in range(5, 15):  # Loop through numbers from 5 to 14 (range excludes 15)

    if number == 8:  # Check if the current number is 8
        print("We are skipping number 8")  # Print message when 8 is encountered
        continue  # Skip the rest of the loop and move to the next iteration

    print("This is the number {}".format(number))  # Print the current number (except 8)


for number in range(5, 15):  # Loop through numbers from 5 to 14 (range excludes 15)

    if number == 8:  # Check if the current number is 8
        pass  # Do nothing if the number is 8 (using 'pass' as a placeholder)

    else:  # For all other numbers
        print("This is the number {}".format(number))  # Print the current number



