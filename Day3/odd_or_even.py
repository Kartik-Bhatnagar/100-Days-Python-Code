
#Write a program that works out whether if a given number is an odd or even number.

number = int(input("Which number do you want to check? "))

num_type ="odd"
if number%2 == 0:
    num_type="even"
print(f"This is an {num_type} number.")
