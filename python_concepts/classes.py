import random  # Importing the random module to generate random numbers


# Define a 'Person' class
class Person:
    # The __init__ method is the "constructor" - it runs every time you create a new person
    def __init__(self, firstname, lastname, health, status):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

        # A method for the person to introduce themselves

    def introduce(self):
        # Print a greeting that includes their first and last name
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    # A method to randomly show the person's emotion for the day
    def emotion(self):
        # Generate a random number between 1 and 2
        emo = random.randrange(1, 3)
        # If the number is 1, the person is happy
        if emo == 1:
            print("{} is happy today".format(self.firstname))
        # If the number is 2, the person is sad
        elif emo == 2:
            print("{} is sad today".format(self.firstname))

    # A method to check the person's health and print a message accordingly
    def status_change(self):
        # If the health is 100, the person is fully healthy
        if self.health == 100:
            print("{} is healthy today!".format(self.firstname))
        # If health is 70 or more but less than 100, the person is tired
        elif self.health >= 70:
            print("{} is a little tired today".format(self.firstname))
        # If health is 50 or less but more than 30, the person feels unwell
        elif self.health <= 50:
            print("{} feels unwell".format(self.firstname))
        # If health is 0, the person is unconscious
        else:
            print("{} is unconscious".format(self.firstname))


# Creating three Person objects with different attributes
Diana = Person("Diana", "Jones", 100, True)  # Diana is a friend and has full health
Daisy = Person("Daisy", "Brown", 75, False)  # Daisy is not a friend and is a bit tired
Jason = Person("Jason", "White", 55, True)  # Jason is a friend and feels unwell

# Print whether Diana is a friend or not
print("Is {} my friend? Status:{}".format(Diana.firstname, Diana.status))

# Calling a method of a class
# Each person introduces themselves
Diana.introduce()
Daisy.introduce()
Jason.introduce()

# Generate and print Diana's emotion for the day (randomly happy or sad)
Diana.emotion()

Diana.status_change()
