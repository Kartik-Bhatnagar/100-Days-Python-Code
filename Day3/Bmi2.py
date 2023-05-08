"""Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese."""


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight/ (height **2)
bmi_type ="have a normal weight"
if bmi <=18.5:
    bmi_type = "are underweight"
elif bmi>35:
    bmi_type ="are clinically obese"
elif bmi >=30:
    bmi_type ="are obese"
elif bmi >=25:
    bmi_type ="are slightly overweight"
print(f"Your BMI is {round(bmi)}, you {bmi_type}.")
