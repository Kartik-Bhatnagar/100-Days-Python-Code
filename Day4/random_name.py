#select a random name from a list of names. The person selected will have to pay for everybody's food bill.

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
print(f"{names[random.randint(0,len(names)-1)]} is going to buy meal today !")
