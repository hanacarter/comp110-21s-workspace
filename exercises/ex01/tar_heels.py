"""An exercise in remainders and boolean logic."""

__author__ = "730406281"


# Begin your solution here...
number: int = int(input("Enter an integer: "))
if number % 2 == 0 or number % 7 == 0:
    if number % 2 == 0 and number % 7 != 0:
        print("TAR")
    if number % 7 == 0 and number % 2 != 0:
        print("HEELS")
    if number % 2 == 0 and number % 7 == 0:
        print("TAR HEELS")
else:
    print("CAROLINA")
