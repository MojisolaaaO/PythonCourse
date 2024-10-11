import random


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
        # If health is 50 or less, the person feels unwell
        elif self.health <= 50:
            print("{} feels unwell".format(self.firstname))
        # If health is 0, the person is unconscious
        else:
            print("{} is unconscious".format(self.firstname))


# Creating three Person objects with different attributes
Diana = Person("Diana", "Jones", 100, True)  # Diana is a friend and has full health
Daisy = Person("Daisy", "Brown", 75, False)  # Daisy is not a friend and is a bit tired
Jason = Person("Jason", "White", 55, True)  # Jason is a friend and feels unwell

Diana.introduce()

class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def introduce(self):
        print("You are my mortal enemy!!!")

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    # the self argument allows access to the enemy,
    # the other argument allows access to the other person being interacted with

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak!".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {} I have your stuff".format(other.firstname))
        if other.status:
            other.status = False


Alex = Enemy('rock', 'Alex', 'Jones', 75, True)

Alex.hurt(Diana)  # Diana's health should reduce by 10

Alex.introduce()