# pip install forex-python

from forex_python.converter import CurrencyRates


# convert amount to amount
def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    result = c.convert(from_currency, to_currency, amount)
    print(f"{from_currency}={amount} to {to_currency}={result}")
    


# root
if __name__ == '__main__':
    amount = int(input('Enter the amount: '))
    from_currency = input('From currency: ').upper()
    to_currency   = input('To currency: ').upper()

    convert_currency(amount, from_currency, to_currency)