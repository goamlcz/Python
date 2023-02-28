import random

for i in range(5):
    kostka1 = random.randint(1, 6)
    kostka2 = random.randint(1, 6)
    soucet = kostka1 + kostka2
    print('Na první kostce padlo číslo:', kostka1)
    print('Na druhé kostce padlo číslo:', kostka2)
    print('Součet obou čísel je:', soucet)
    print()

