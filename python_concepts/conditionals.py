"""
Comparison operators allow comparison between two values
The result is either True or False
less than (<)
less than or equal to (<=)
greater than (>)
greater than or equal to (>=)
equal to (==)
not equal to (!=)

Conditions are statement that allows us to make decisions
within our code based on a given set of conditions

if statement shows code that should run only if certain conditions are present
elif statement shows code that should run if conditions before are not met
else statement closes out the if, elif, else code block
and contains anything the user might not do
"""

name = input("What is your name? ")
if name == "Mojisola":
    print("Hello {}!".format(name))
elif name == "Diana":
    print("You are pretty")
elif name == "Molade":
    print("Nice to meet you {}".format(name))
else:
    print("Have a nice day!")
