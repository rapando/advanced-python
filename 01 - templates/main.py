"""
This is the code for Templates
"""

from string import Template


class MyTemplate(Template):
    # The default delimiter is $. Use this to change this.
    delimiter = '#'


if __name__ == "__main__":
    cart = []
    cart.append(dict(item="Coke", price=8, qtty=2))
    cart.append(dict(item="Cake", price=12, qtty=1))
    cart.append(dict(item="Fish", price=32, qtty=4))

    temp = MyTemplate("#qtty x #item = #price")
    total = 0
    print("Cart : ")

    for data in cart:
        print(temp.substitute(data))
        total += data['price']

    print("Total : ", total)
