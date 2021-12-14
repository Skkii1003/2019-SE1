"""write your code in method currency_exchange"""
def currency_exchange():
    money = float(input("How many eruos are you exchanging?"))
    rate = float(input("What is the exchange rate?"))
    print('{0:.2f} euros at an exchange rate of {1:.2f} is {2:.2f} U.S. dollars.'.format(money, rate, money * rate / 100))
    return 0