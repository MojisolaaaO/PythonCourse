def days_of_the_week():
    a = input("What is the first day of the week? ")

    if a == "Monday":
        print("Correct! {} is the first day of the week".format(a))
    elif a == "Tuesday":
        print("Incorrect! {} is the second day of the week ".format(a))
    elif a == "Wednesday":
        print("Incorrect! {} is the third day of the week ".format(a))
    elif a == "Thursday":
        print("Incorrect! {} is the fourth day of the week ".format(a))
    elif a == "Friday":
        print("Incorrect! {} is the fifth day of the week ".format(a))
    elif a == "Saturday":
        print("Incorrect! {} is the sixth day of the week ".format(a))
    elif a == "Sunday":
        print("Incorrect! {} is the seventh day of the week ".format(a))
    else:
        print("That is not a day of the week")


# days_of_the_week()


def user_profile(name, gender):
    print("{} is a {}".format(name, gender))


# user_profile('Moji', "Female")


def numbers():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    if a == b:
        print("Same number")
    elif a > b:
        print("{} is greater than {} ".format(a, b))
    elif a < b:
        print("{} is less than {} ".format(a, b))
    elif a != b:
        print("{} is not equal to {} ".format(a, b))


numbers()






