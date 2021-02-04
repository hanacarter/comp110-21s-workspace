"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730406281"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
fortune: int = randint(1,4)

if fortune < 3:
    if fortune == 2:
        print("Today is gonna be YOUR day!!")
    else:
        print("This is the perfect time in your life to travel.")
else:
    if fortune < 4:
        print("You will find happiness once you drop out of college :'))")
    else:
        print("You will soon qualify for the US Olymic bobsledding team :D")

print("Now, go spread positive vibes!")
