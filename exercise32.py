# Title Exercise 32
# Author: Benjamin Lemery
# Date: 10/14/2019
# This program is designed to run through various loops

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies',2,'dimes',3,'quarters']

# This first kind of for-loop goes through a list.
for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = []

for i in range(0,6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")

