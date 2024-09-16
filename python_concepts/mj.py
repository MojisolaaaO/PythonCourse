Data = ["Mojisola", "Otusheso", 24, "2000-04-29"]
print(Data)

Data.append("Nigerian")
print(Data)


Data.insert(5, "QA")
print(Data)


def numbers():
    a = int(input("Enter a number "))
    if a < 0:
        print("Enter another number")
        numbers()
    elif a > 0:
        print("{} is a valid number".format(a))


numbers()
