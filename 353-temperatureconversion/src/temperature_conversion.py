from math import floor


def convert_temperature():
    type = input("Your choice: ")
    if type=="C":
        f = float(input("Please enter the temperature in Fahrenheit: "))
        c = (f-32)*5/9
        print("The temperature in Celsius is {:d}.".format(floor(c)))
    if type=="F":
        c = float(input("Please enter the temperature in Celsius: "))
        f = (c*9/5)+32
        print("The temperature in Fahrenheit is {:d}.".format(floor(f)))
