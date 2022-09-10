# Create array of alcohol and non-alcohol drinks

alco_drinks = ["BEER", "wine", "vodka"]
non_alco_drinks = ["water", "juice"]


def print_random_drink(alco_drinks_arr, non_alco_drinks_arr):
    import random

    # Print bla bla bla and 2 random drinks in single line

    print("бла бла бла", random.choice(alco_drinks_arr), "and", random.choice(non_alco_drinks_arr))


print_random_drink(alco_drinks, non_alco_drinks)
print("bla bla bla")

