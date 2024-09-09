# Positional Arguments - the arguments are passed to a function in a specific order
def user_info(name, age, city):
    # This function prints name, age and city from an argument provided to the function

    print("{} is {} years old from {}".format(name, age, city))


user_info("Moji", 24, "LA")


# Keyword Arguments - passed with the name of the parameter (key) along with its value
# the order does not matter
def user_info(name, gender="female", country="USA"):
    print("{} is a {} from {}".format(name, gender, country))


user_info("Moji")
user_info(gender="male", name="June")

'''
*args is used for positional arguments
allows a function to take any number of positional arguments  

 **kwargs  is used for keyword arguments
allows a function to take any number of keyword arguments
'''


def add(*args):
    print(sum(args))


add(2, 3, 4)


def apply(name, email, **kwargs):
    print("Her name is {} and her email is {}".format(name, email))

    # Print the keyword arguments (**kwargs)

    if kwargs:
        print("Additional info:", kwargs)


apply(name="Moji", email="moji@gmail.com", job="QA")

'''
all three argument types can be used in a single function 
they must be used in order: positional, *args, **kwargs
'''


def application(firstname, lastname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(firstname, lastname, company, email))

    # Print the additional positional arguments (*args)
    if args:
        print("Additional information (args):", args)

    # Print the keyword arguments (**kwargs)
    if kwargs:
        print("Additional information (kwargs):", kwargs)


application("Mojisola", "Otusheso", "moji@gmail.com", "Lodgify", 1000000, hire_date="October 1st")
