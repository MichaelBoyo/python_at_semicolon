class MaxBasketSize:

    def __init__(self, size):
        self.size = size
        self.basket = []

    def buy_item(self, item):
        if len(self.basket) > self.size-1:
            self.basket.pop(0)
            self.basket.append(item)
            return
        self.basket.append(item)

    @property
    def items(self):
        return self.basket


my_basket = MaxBasketSize(4)

my_basket.buy_item("broom")
my_basket.buy_item("shoe")
my_basket.buy_item("bag")
my_basket.buy_item("cup")
my_basket.buy_item("stick")

print(my_basket.items)
