import decimal
from decimal import Decimal


def bmi():
    print('Write your code here.')


def decimal_retain(number, ndigits=0):
    """
    Round a number to a given precision in decimal digits (default 0 digits).
    The strategy is : Low values rounded up.
    :param number: The number needed to be rounded.
    :param ndigits: The number of digits.
    :return: The number after being rounded.
    """
    context = decimal.getcontext()
    context.rounding = decimal.ROUND_UP
    return round(Decimal(str(number)), ndigits)
