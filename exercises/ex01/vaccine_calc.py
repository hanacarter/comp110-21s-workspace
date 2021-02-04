"""A vaccination calculator."""

__author__ = "730406281"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
Population: int = int(input("Population: "))
Doses_admin: int = int(input("Doses administered: "))
Doses_per_day: int = int(input("Doses per day: "))
Target: int = int(input("Target percent vaccinated: "))
Today: datetime = datetime.today()
x: float = (Target / 100) * Population
y: int = round((x - (Doses_admin / 2)) / (Doses_per_day / 2))
Day: timedelta = timedelta(y)
Done: datetime = Today + Day
print("We will reach " + str(Target) + "% vaccination in " + str(Day) + " which falls on " + (Done.strftime("%B %d, %Y")))
