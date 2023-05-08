#Write a program that adds the digits in a 2 digit number


two_digit_number = int(input("Type a two digit number: "))

num1 = two_digit_number %10
num2 = two_digit_number //10
print(num1+num2)
