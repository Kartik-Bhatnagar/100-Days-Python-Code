#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age? ")

age_left = 90-int(age)
print(f"You have {age_left*365} days, {(age_left)*(365//7)} weeks, and {age_left*12} months left.")
