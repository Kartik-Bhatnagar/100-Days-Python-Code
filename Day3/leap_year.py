""" This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 

**except** every year that is evenly divisible by 100 

**unless** the year is also evenly divisible by 400"""
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leap =False
if (year%100 ==0):
    if year%400 == 0:
        leap =True
    else:
        leap = False
else:
    if year%4 == 0:
        leap = True
    else:
        leap =False      

if leap:
    print("Leap year.")
else:
    print("Not leap year.")    
