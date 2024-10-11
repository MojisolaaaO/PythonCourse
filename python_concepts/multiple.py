# Parent class 1
class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}".format(self.sku))


# Parent class 2
class Garment():
    def __init__(self, section, garment_type):
        self.section = section
        self.garment_type = garment_type

    def print_garment(self):
        print("The garment is in section {}".format(self.section))


# Child class
class Shirts(Item, Garment):
    def __init__(self, sku, section, garment_type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, garment_type)

    def print_shirt(self):
        print("{} {} is on sale".format(self.color, self.name))


# Creating an object of Shirts class
Blouse = Shirts("00001", 43, "Tops", "Formal Blouse", "White")

# Calling methods
Blouse.print_sku()       # Should print: The sku is 00001
Blouse.print_garment()   # Should print: The garment is in section 43
Blouse.print_shirt()     # Should print: White Formal Blouse is on sale
