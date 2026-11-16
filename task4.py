"""
# Task 4
# Access list values


Ask the user to enter in a number less than 10
Print out the list element that corresponds to that
position in the tuple
"""

people = ("John","Tyler","Dash","Kieran","Jayson","Tomoki","Minji","Dawson","Hewitt","Josh","Anson","Cole")

num = int(input("Enter number to get from list: "))

if num > 10 or num < 1:
    num = 1

for i in people:
    if people[num-1] == i:
        print(people[num-1])