class MaxBasketSize:

    def __init__(self, size):
        self.size = size
        self.basket = []

    def buy_item(self, item):
        self.basket.append(item)
        if len(self.basket) > self.size:
            self.basket.pop(0)


class Bas2(MaxBasketSize):
    pass


my_basket = Bas2(4)

my_basket.buy_item("broom")
my_basket.buy_item("shoe")
my_basket.buy_item("bag")
my_basket.buy_item("cup")
my_basket.buy_item("stick")

print(my_basket.basket)
