def make_sandwich(*ingredients):
    print(f"\nThe ingredients are:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('bread')
make_sandwich('bread','meat','tomatoe')
make_sandwich('bread','meat','tomatoe','cheese')

