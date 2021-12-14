"""write your code in method currency_exchange"""
def currency_exchange():
    money = int (input("How many eruos are you exchanging?"))
    rate = float (input("What is the exchange rate?"))
    print('{0:d} euros at an exchange rate of {1:.2f} is {2:.2f} U.S. dollars.'.format(money,rate,money*rate/100))
    #homework 01
    return 0