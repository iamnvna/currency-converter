from forex_python.converter import CurrencyRates, RatesNotAvailableError

c = CurrencyRates()

amount = int(input("Enter the amount: "))
from_currency = input("From Currency (Eg. USD): ").upper()
to_currency = input("To Currency (Eg. EUR): ").upper()

print("\nProcessing ...")

try:
    result = round(c.convert(from_currency, to_currency, amount), 2)
    print(f"{amount} {from_currency} is {result} {to_currency}")
except RatesNotAvailableError:
    print("Oops! Rate not available.")

# Commentary
'''
Line 1:
    Line 1 is essential to this code. It module used is installed
    with the 'pip install forex-python' command through the terminal.
    This module provides methods that allow the code to convert
    from one currency to another, or perform other functions. The
    full details is in th documentation.
    
Line 5-7:
    This block of code accepts the required inputs from the user
    to perform this function.

Line 9:
    Rates are returned between 1-5s. This print statement informs
    the user of the ongoing background process.

Line 11-15:
    This block of code, manages error from rates that are not currently
    available through the error handling python technique. The 'convert'
    method, accepts the parameters from the user, and performs a conversion.
    The result is rounded to two decimal places, and printed out for the
    user.
'''