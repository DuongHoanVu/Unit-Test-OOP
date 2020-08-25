from shirt_modular import Shirt

shirt_one = Shirt('red', 'S', 'long-sleeve', 25)

print(shirt_one.price)
shirt_one.change_price(10)
print(shirt_one.price)
print(shirt_one.discount(.12))

shirt_two = Shirt('orange', 'L', 'short-sleeve', 10)

total = shirt_one.price + shirt_two.price

total_discount =  shirt_one.discount(.14) + shirt_two.discount(.06) 


# TEST THE PROGRAM ABOVE
from tests import run_tests

run_tests(shirt_one, shirt_two, total, total_discount)